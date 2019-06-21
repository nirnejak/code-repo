import textwrap


def merge_the_tools(string, k):
    substrings = textwrap.wrap(string, k)
    result = []

    # Calculating ui
    for ti in substrings:
        # Initializing ui with first letter of ti
        ui = [ti[0]]
        # Checking and adding character at a time
        for i in ti:
            if i not in ui:
                ui.append(i)

        ui = ''.join(ui)
        result.append(ui)

    for i in result:
        print(i)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
