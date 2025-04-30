#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <pthread.h>

#define BUFFER_SIZE 1024

typedef struct {
    int sock;
    char username[50];
} Client;

void *receive_messages(void *arg) {
    Client *client = (Client *)arg;
    char buffer[BUFFER_SIZE];

    while (recv(client->sock, buffer, sizeof(buffer) - 1, 0) > 0) {
        printf("%s", buffer);
        fflush(stdout);
    }

    printf("\nConnection closed.\n");
    exit(0);
}

int main(int argc, char *argv[]) {
    if (argc != 7 || strcmp(argv[1], "--ip") != 0 || strcmp(argv[3], "--port") != 0 || strcmp(argv[5], "--name") != 0) {
        fprintf(stderr, "Usage: %s --ip <ip_address> --port <port> --name <username>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    const char *ip = argv[2];
    int port = atoi(argv[4]);
    const char *username = argv[6];

    int sock;
    struct sockaddr_in server_addr;

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    inet_pton(AF_INET, ip, &server_addr.sin_addr);

    if (connect(sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection failed");
        close(sock);
        exit(EXIT_FAILURE);
    }

    // Send username to server
    send(sock, username, strlen(username), 0);

    // Create a thread to handle incoming messages
    pthread_t recv_thread;
    Client client = {sock};
    strncpy(client.username, username, sizeof(client.username) - 1);
    pthread_create(&recv_thread, NULL, receive_messages, &client);
    pthread_detach(recv_thread);

    // Handle user input
    char buffer[BUFFER_SIZE];
    while (fgets(buffer, sizeof(buffer), stdin) != NULL) {
        if (strncmp(buffer, "/quit", 5) == 0) {
            break;
        }

        char msg[BUFFER_SIZE];
        snprintf(msg, sizeof(msg), "<%s> %s", username, buffer);
        send(sock, msg, strlen(msg), 0);
    }

    close(sock);
    return 0;
}
