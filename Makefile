install-depends:
	sudo apt install git python3 mpg123 wildmidi ranger gcc
	git clone http://154.64.231.77:3000/Yukari/Minesweeper
	cd Minesweeper
	make
	cd ..

run:
	python3 pyosimproved.py
