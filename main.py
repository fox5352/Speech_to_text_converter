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
    transcript = list()

    stt = Converter()

    said_exit = False
    
    # process pipeline and list
    # processes = []
    parent_pipe, child_pipe = multiprocessing.Pipe()

    while not said_exit:
        print("listening...")
        audio = stt.listener()
        
        text = stt.converter(audio)
        print(text)
        transcript.append(text)

        # if the transcript is not empty
        # if the transcript has the word exit in it ends all process and exit program
        if len(transcript) > 0:
            for sentence in transcript:
                if "exit" in sentence:
                    said_exit = True

    # asks to save the transcript to a file
    save_file = input("save data to file y/n :")

    # save the transcript to a file with the input data
    if save_file.lower() == "y":
        save_to_file(transcript[0:-1], input("file name: "))

if __name__ == "__main__":
    main()
    print("EOP")
