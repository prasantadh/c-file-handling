main: main.c 
	gcc -Wextra -Wall --std c2x $^ -o $@

clean: 
	rm main
