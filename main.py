from Audio_converter import Converter
# Local files ^
import multiprocessing


def file_writer(file_name, transcript):
    with open(f'{file_name}.txt', "a") as file:
        for line in transcript:
            file.write(f'{line}\n')

    print(f'{file_name}.txt successfully created')   


def save_to_file(transcript, file_name) -> None:
    with open(f'{file_name}.txt', "w") as file:
        for line in transcript:
            file.write(f'{line}\n')
    return


def main():
    transcript = []

    stt = Converter()

    said_exit = False
    
    # process pipeline and list
    processes = []
    parent_pipe, child_pipe = multiprocessing.Pipe()

    while not said_exit:
        print("listening...")
        audio = stt.listener()
        

        # creates a process with a pipeline 
        p = multiprocessing.Process(target=stt.converter, args=(audio, child_pipe))
        # starts the conversion on that process
        p.start()
        # adds the process to the list of processes
        processes.append(p)

        # checks if the pipeline signals the process is finished
        # retrieves the data from the process and writes it to the transcript 
        if parent_pipe.poll():            
            data = parent_pipe.recv()
            transcript.append(data)
        
        # if the transcript is not empty
        # if the transcript has the word exit in it ends all process and exit program
        if len(transcript) > 0:
            if transcript[len(transcript) - 1] == "exit":
                said_exit = True
                for p in processes:
                    p.terminate()
                break

    # asks to save the transcript to a file
    save_file = input("save data to file y/n :")

    # save the transcript to a file with the input data
    if save_file.lower() == "y":
        save_to_file(transcript[0:-1], input("file name: "))


if __name__ == "__main__":
    main()
    print("EOP")
