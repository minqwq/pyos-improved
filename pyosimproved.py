import time as tm
import getpass
import datetime
import calendar
import os
import sys
import time
import socket
import struct
import select
# Preload classes
#
# How to use these color:
# green for example
# use this trick:
# (color.green + "text here" + color.reset)
# if you want use other color, change "green" to any below name on class color
# color.<color>
class color: # Text colors
    red = "\033[31m"
    green = "\033[32m"
    blue = "\033[34m"
    yellow = "\033[33m"
    purple = "\033[35m"
    cyan = "\033[36m"
    grey = "\033[37m"
    reset = "\033[0m"
class text:
    error = color.red + "[!] " + color.reset
# BIOS Animation
print("cleaning screen...") # Clean screen first
i = os.system("cls")
i = os.system("clear")
time.sleep(0.5)
print("Press F1 for BIOS Setup")
time.sleep(1)
i = os.system("cls")
i = os.system("clear")
print("Press F1 for BIOS Setup.")
time.sleep(1)
i = os.system("cls")
i = os.system("clear")
print("Press F1 for BIOS Setup..")
time.sleep(1)
i = os.system("cls")
i = os.system("clear")
print("Press F1 for BIOS Setup...")
time.sleep(1)
i = os.system("cls")
i = os.system("clear")
i = os.system("mpg123 -q ./beep.mp3") # *beep*
print("Access BIOS v8.2")
print("bios.mcpestudio.com/release/8/2/0/index.html")
time.sleep(0.3)
print(color.yellow + "Testing Memory..." + color.reset)
time.sleep(0.5)
print(color.green + "512MB OK" + color.reset)
time.sleep(0.1)
print(color.yellow + "Booting From Hard Disk..." + color.reset)
time.sleep(1)
i = os.system("cls")
i = os.system("clear")
time.sleep(0.1)
# Startup screen
print("  ______   __     ___  ____  ")
print(" |  _ \ \ / /    / _ \/ ___| ")
print(" | |_) \ V /    | | | \___ \ ")
print(" |  __/ | |     | |_| |___) |")
print(" |_|    |_|      \___/|____/ ")
print(color.purple + "      --- Improved ---       " + color.reset)
print(" ")
print(text.error + color.red + "Under development, may be unstable")
print("\033[31mPY\033[0m \033[33mOS\033[0m \033[34mImproved\033[0m | Version 1.0(Beta 1 | Build 18)")
print("Original by AMDISYES | Improved Version by minqwq ヽ(✿ﾟ▽ﾟ)ノ")
print("This screen will show 5 second")
print(" ")
print("Make sure always are latest version!")
print("Update trick:shutdown PY OS Improved and type 'git pull' on pyos-improved folder to update system")
print(" ")
print("Current source code lines:196")
time.sleep(5)
i = os.system("cls")
i = os.system("clear")
time.sleep(0.1)
print(color.grey + "[INFO] Begin of logging" + color.reset) # System loader screen
time.sleep(0.05)
print(color.yellow + "[...] Waking up system-process..." + color.reset)
time.sleep(0.25)
print(color.green + "[O] system-process is waked up" + color.reset)
time.sleep(0.1)
print(color.yellow + "[...] Detecting hardwares..." + color.reset)
time.sleep(0.5)
print(color.green + "[O] Hardware list updated" + color.reset)
time.sleep(0.05)
print(color.yellow + "[...] Waking up user-manager" + color.reset)
time.sleep(0.1)
print(color.yellow + "[...] Waking up login-manager" + color.reset)
time.sleep(0.2)
print(color.green + "[O] user-manager is waked up" + color.reset)
time.sleep(0.1)
print(color.green + "[O] login manager is waked up" + color.reset)
time.sleep(0.5)
i = os.system("cls")
i = os.system("clear")
time.sleep(0.1)
i = os.system("mpg123 -q ./startup.mp3")
print(color.green + "Hi~ o(*￣▽￣*)ブ My master~ Welcome back to PY OS Improved~" + color.reset) # Login screen
count = 0
stpasswd = "45450721"
while count < 3:
    user = input("Account login: ")
    if user == "root":
        i = os.system("mpg123 -q ./beep.mp3")
        print(color.yellow + "This account has been protected by password, please type password(45450721)" + color.reset)
        while count < 3:
            passwd = getpass.getpass("Password: ")
            if passwd == stpasswd:
                i = os.system("mpg123 -q beep.mp3")
                tm.sleep(1.5)
                while count < 3:
                    cmd = input("root@pyosi (Unknown path) > ") # Shell style(redesigned by minqwq)
                    if cmd == "ls": # Path
                        print(text.error + color.red + "Path not found" + color.reset)
                    elif cmd == "neofetch": # a Fake neofetch
                        print("  ______   __     ___  ____  ")
                        print(" |  _ \ \ / /    / _ \/ ___| ")
                        print(" | |_) \ V /    | | | \___ \ ")
                        print(" |  __/ | |     | |_| |___) |")
                        print(" |_|    |_|      \___/|____/ ")
                        print(color.purple + "      --- Improved ---       " + color.reset)
                        time.sleep(0.1)
                        print("System:PY OS Improved 1.0 b1 b18")
                        time.sleep(0.1)
                        print("CPU:Intel Pentium 4@1400MHz")
                        time.sleep(0.1)
                        print("GPU:Cirrus Logic GD 5446(4MB)")
                        time.sleep(0.1)
                        print("Memory:512MB DDR2")
                        time.sleep(0.1)
                        print("Sound Card:Speaker")
                        time.sleep(0.1)
                        print(text.error + color.red + "Ethernet Card:Not found" + color.reset)
                        time.sleep(0.1)
                        print("Disk:HDD1=30GB, HDD2=55GB")
                    elif cmd == "ping": # Ping tool
                        print(text.error + color.red + "Unavailable for now" + color.reset)
                        def checksum(data):
                            """Creates the ICMP checksum as in RFC 1071
                        
                            :param data: Data to calculate the checksum ofs
                            :type data: bytes
                            :return: Calculated checksum
                            :rtype: int
                        
                            Divides the data in 16-bits chunks, then make their 1's complement sum"""
                            subtotal = 0
                            for i in range(0, len(data)-1, 2):
                                subtotal += ((data[i] << 8) + data[i+1])                # Sum 16 bits chunks together
                            if len(data) % 2:                                           # If length is odd
                                subtotal += (data[len(data)-1] << 8)                    # Sum the last byte plus one empty byte of padding
                            while subtotal >> 16:                                       # Add carry on the right until fits in 16 bits
                                subtotal = (subtotal & 0xFFFF) + (subtotal >> 16)
                            check = ~subtotal                                           # Performs the one complement
                            return ((check << 8) & 0xFF00) | ((check >> 8) & 0x00FF)    # Swap bytes
                        
                        
                        class ICMPType:
                            """Represents an ICMP type, as combination of type and code
                        
                            ICMP Types should inherit from this class so that the code can identify them easily.
                            This is a static class, not meant to be instantiated"""
                            def __init__(self):
                                raise TypeError('ICMPType may not be instantiated')
                        
                        
                        class Types(ICMPType):
                            class EchoReply(ICMPType):
                                type_id = 0
                                ECHO_REPLY = (type_id, 0,)
                        
                            class DestinationUnreachable(ICMPType):
                                type_id = 3
                                NETWORK_UNREACHABLE = (type_id, 0,)
                                HOST_UNREACHABLE = (type_id, 1,)
                                PROTOCOL_UNREACHABLE = (type_id, 2,)
                                PORT_UNREACHABLE = (type_id, 3,)
                                FRAGMENTATION_REQUIRED = (type_id, 4,)
                                SOURCE_ROUTE_FAILED = (type_id, 5,)
                                NETWORK_UNKNOWN = (type_id, 6,)
                                HOST_UNKNOWN = (type_id, 7,)
                                SOURCE_HOST_ISOLATED = (type_id, 8,)
                                NETWORK_ADMINISTRATIVELY_PROHIBITED = (type_id, 9,)
                                HOST_ADMINISTRATIVELY_PROHIBITED = (type_id, 10,)
                                NETWORK_UNREACHABLE_TOS = (type_id, 11,)
                                HOST_UNREACHABLE_TOS = (type_id, 12,)
                                COMMUNICATION_ADMINISTRATIVELY_PROHIBITED = (type_id, 13,)
                                HOST_PRECEDENCE_VIOLATION = (type_id, 14,)
                                PRECEDENCE_CUTOFF = (type_id, 15,)
                        
                            class SourceQuench(ICMPType):
                                type_id = 4
                                SOURCE_QUENCH = (type_id, 0,)
                        
                            class Redirect(ICMPType):
                                type_id = 5
                                FOR_NETWORK = (type_id, 0,)
                                FOR_HOST = (type_id, 1,)
                                FOR_TOS_AND_NETWORK = (type_id, 2,)
                                FOR_TOS_AND_HOST = (type_id, 3,)
                        
                            class EchoRequest(ICMPType):
                                type_id = 8
                                ECHO_REQUEST = (type_id, 0,)
                        
                            class RouterAdvertisement(ICMPType):
                                type_id = 9
                                ROUTER_ADVERTISEMENT = (type_id, 0,)
                        
                            class RouterSolicitation(ICMPType):
                                type_id = 10
                                ROUTER_SOLICITATION = (type_id, 0)
                                # Aliases
                                ROUTER_DISCOVERY = ROUTER_SOLICITATION
                                ROUTER_SELECTION = ROUTER_SOLICITATION
                        
                            class TimeExceeded(ICMPType):
                                type_id = 11
                                TTL_EXPIRED_IN_TRANSIT = (type_id, 0)
                                FRAGMENT_REASSEMBLY_TIME_EXCEEDED = (type_id, 1)
                        
                            class BadIPHeader(ICMPType):
                                type_id = 12
                                POINTER_INDICATES_ERROR = (type_id, 0)
                                MISSING_REQUIRED_OPTION = (type_id, 1)
                                BAD_LENGTH = (type_id, 2)
                        
                            class Timestamp(ICMPType):
                                type_id = 13
                                TIMESTAMP = (type_id, 0)
                        
                            class TimestampReply(ICMPType):
                                type_id = 14
                                TIMESTAMP_REPLY = (type_id, 0)
                        
                            class InformationRequest(ICMPType):
                                type_id = 15
                                INFORMATION_REQUEST = (type_id, 0)
                        
                            class InformationReply(ICMPType):
                                type_id = 16
                                INFORMATION_REPLY = (type_id, 0)
                        
                            class AddressMaskRequest(ICMPType):
                                type_id = 17
                                ADDRESS_MASK_REQUEST = (type_id, 0)
                        
                            class AddressMaskReply(ICMPType):
                                type_id = 18
                                ADDRESS_MASK_REPLY = (type_id, 0)
                        
                            class Traceroute(ICMPType):
                                type_id = 30
                                INFORMATION_REQUEST = (type_id, 30)
                        
                                                
                        class ICMP:
                            LEN_TO_PAYLOAD = 41     # Ethernet, IP and ICMP header lengths combined
                        
                            def __init__(self, message_type=Types.EchoReply, payload=None, identifier=None, sequence_number=1):
                                """Creates an ICMP packet
                        
                                :param message_type: Type of ICMP message to send
                                :type message_type: Union[ICMPType, (int, int), int]
                                :param payload: utf8 string or bytes payload
                                :type payload: Union[str, bytes]
                                :param identifier: ID of this ICMP packet
                                :type identifier: int"""
                                self.message_code = 0
                                if issubclass(message_type, ICMPType):
                                    self.message_type = message_type.type_id
                                elif isinstance(message_type, tuple):
                                    self.message_type = message_type[0]
                                    self.message_code = message_type[1]
                                elif isinstance(message_type, int):
                                    self.message_type = message_type
                                if payload is None:
                                    payload = bytes('1', 'utf8')
                                elif isinstance(payload, str):
                                    payload = bytes(payload, 'utf8')
                                self.payload = payload
                                if identifier is None:
                                    identifier = os.getpid()
                                self.id = identifier & 0xFFFF           # Prevent identifiers bigger than 16 bits
                                self.sequence_number = sequence_number
                                self.received_checksum = None
                        
                            @property
                            def packet(self):
                                """The raw packet with header, ready to be sent from a socket"""
                                return self._header(check=self.expected_checksum) + self.payload
                        
                            def _header(self, check=0):
                                """The raw ICMP header
                        
                                :param check: Checksum value
                                :type check: int
                                :return: The packed header
                                :rtype: bytes"""
                                # TODO implement sequence number
                                return struct.pack("bbHHh",
                           self.message_type,
                           self.message_code,
                           check,
                           self.id,
                           self.sequence_number)
                        
                            @property
                            def is_valid(self):
                                """True if the received checksum is valid, otherwise False"""
                                if self.received_checksum is None:
                                    return True
                                return self.expected_checksum == self.received_checksum
                        
                            @property
                            def expected_checksum(self):
                                """The checksum expected for this packet, calculated with checksum field set to 0"""
                                return checksum(self._header() + self.payload)
                        
                            @property
                            def header_length(self):
                                """Length of the ICMP header"""
                                return len(self._header())
                        
                            @staticmethod
                            def generate_from_raw(raw):
                                """Creates a new ICMP representation from the raw bytes
                        
                                :param raw: The raw packet including payload
                                :type raw: bytes
                                :return: An ICMP instance representing the packet
                                :rtype: ICMP"""
                                packet = ICMP()
                                packet.unpack(raw)
                                return packet
                        
                            def unpack(self, raw):
                                """Unpacks a raw packet and stores it in this object
                                                
                                :param raw: The raw packet, including payload
                                :type raw: bytes"""
                                self.message_type, \
                                    self.message_code, \
                                    self.received_checksum, \
                                    self.id, \
                                    sequence = struct.unpack("bbHHh", raw[20:28])
                                self.payload = raw[28:]
                    elif cmd == "sudo": # sudo not sudo
                        print("This system is not based on linux, so sudo is not on here")
                    elif cmd == "about": # About system
                        print("---------------| About |---------------")
                        print(color.blue + "PY OS Improved 1.0 b1(Build 18)" + color.reset)
                        print(color.grey + "(C) 0x1c Studio 2022--2023 | (C) LR Studio 2024" + color.reset)
                    elif cmd == "shutdown": # Shutdown
                        i = os.system("mpg123 -q ./shutdown.mp3")
                        print(color.yellow + "[...] Killing all process..." + color.reset)
                        time.sleep(1)
                        sys.exit()
                    elif cmd == "converter": # converter but cant select file
                        print("File Convert\nConvert .lpap/.lpcu/.bbc to .umm")
                        input("Input file's path:\n")
                        for i in range(1, 101):
                            print("\r", end="")
                            print("Progress: {}%: ".format(i), "=" * (i // 2), end="")
                            sys.stdout.flush()
                            tm.sleep(0.05)
                        print("\nConvert Complete")
                    elif cmd == "time": # Show current time
                        now = datetime.datetime.now()
                        other_StyleTime = now.strftime("\nCurrent time:%Y-%m-%d %H:%M:%S")
                        print(other_StyleTime)
                    elif cmd == "passwd": # Change password(for this session)
                        stpasswd = input("Input new password of this account: ")
                    elif cmd == "calendar": # Calendar
                        yy = int(input("Year: "))
                        mm = int(input("Month: "))
                        print(calendar.month(yy, mm))
                    elif cmd == "help": # Command list
                        print("Command List:")
                        print(color.cyan + "ls             View the path")
                        print("about          Show the system's information")
                        print("converter      A tool to convert .lpap/.lpcu/.bbc to .umm")
                        print("time           Show the time and date")
                        print("calendar       Show a calendar")
                        print("calc           A simple calculator")
                        print("clear          Clean the screen")
                        print("passwd         Change your password")
                        print("exit           Log out")
                        print("shutdown       Shutdown system")
                        print("neofetch       List all hardware and system version")
                        print("sudo           Nothing")
                        print("ping           Ping tool python version(Unavailable)" + color.reset)
                    elif cmd == "calc": # Calculator
                        try:
                            formula = input("Enter the formula to be calculated(example:1+1):\n")
                            print(formula + "=", eval(formula))
                        except Exception as e:
                            print("Input error.")
                    elif cmd == "": # what is this??? --minqwq at 2024-06-12 19:32
                        space = "0"
                    elif cmd == "clear": # Clear screen using real system command
                        i = os.system("cls")
                        i = os.system("clear")
                    elif cmd == "exit": # Logout
                        break
                    else: # Wrong command
                        print(text.error + color.red + "Shell:Command not found." + color.reset)
            else: # Wrong password
                print(color.red + "Password Incorrect, please try again" + color.reset)
    else: # Wrong user name
        print(color.red + "User not found, try another" + color.reset)
