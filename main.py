from Audio_converter import Converter
# Local files ^
import multiprocessing
import time


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
    processes = []
    parent_pipe, child_pipe = multiprocessing.Pipe()

    while not said_exit:
        print("listening...")
        audio = stt.listener()

        p = multiprocessing.Process(target=stt.converter, args=(audio, child_pipe))
        p.start()
        processes.append(p)

        if parent_pipe.poll():
            data = parent_pipe.recv()
            transcript.append(data)

        if len(transcript) > 0:
            if transcript[len(transcript) - 1] == "exit":
                said_exit = True
                for p in processes:
                    p.terminate()
                break

    save_file = input("save data to file y/n :")

    if save_file.lower() == "y":

        save_to_file(transcript[0:-1], input("file name: "))


if __name__ == "__main__":
    main()
