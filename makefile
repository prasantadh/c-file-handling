main: main.c 
	gcc -Wextra -Wall --std c2x $^ -o $@ && ./main data.bin

clean: 
	rm main
