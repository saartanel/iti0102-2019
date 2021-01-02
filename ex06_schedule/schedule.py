"""Create schedule from the given file."""
import re


def read_file(input_file):
    """
    Reading from file.

    :param input_file:
    """
    with open(input_file, "r") as file:
        data = file.read()
        return data


def get_schedule_dict(input_string):
    """
    Creating dict.

    :param input_string:
    """
    schedule_dict = {}
    regex = r" ([0-9]+)\D([0-9]+)\ +([a-zA-Z]+)"
    for match in re.finditer(regex, input_string):
        h = match.group(1)
        m = match.group(2)
        w = match.group(3).lower()
        if len(h) <= 2 and len(m) <= 2:
            if 0 <= int(h) < 24 and 0 <= int(m) <= 59:
                t = f"{int(h):02}:{int(m):02}"
                if t in schedule_dict:
                    value_list = []
                    for i in schedule_dict[t]:
                        value_list.append(i)
                    if w not in value_list:
                        value_list.append(w)
                    schedule_dict[t] = value_list
                else:
                    schedule_dict[t] = [w]
    return schedule_dict


def get_am_pm(input_string):
    """
    Get am/pm list.

    :param input_string:
    """
    schedule_dict = get_schedule_dict(input_string)
    sorted_dict = {}
    for i in sorted(schedule_dict):
        sorted_dict[i] = schedule_dict[i]
    ampm_dict = {}
    for i in sorted_dict:
        hour = i.split(":", )[0]
        hour = int(hour)
        time_list = i.split(":")
        words = schedule_dict[i]
        if 0 <= hour < 12:
            if hour == 0:
                time_list[0] = "12"
            else:
                time_list[0] = "%02d" % hour
            t = time_list[0] + ":" + time_list[1] + " AM"
            ampm_dict[t.lstrip("0")] = words
        else:
            if hour == 12:
                time_list[0] = "12"
            else:
                time_list[0] = "%02d" % (hour - 12)
            t = time_list[0] + ":" + time_list[1] + " PM"
            ampm_dict[t.lstrip("0")] = words
    return ampm_dict


def get_table_space(key_value, number):
    """
    Calculate max len number from a list of dict key and value lengths.

    :param key_value:
    :param number:
    """
    length = [number]
    for i in key_value:
        if type(i) == str:
            length.append(len(i))
        else:
            if len(i) > 1:
                length.append(len(', '.join(i)))
            else:
                length.append(len(i[0]))
    return max(length) + 2


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    ampm_dict = get_am_pm(input_string)
    if len(ampm_dict) == 0:
        return "------------------\n|  time | items  |\n------------------\n| No items found |\n------------------"
    w1 = get_table_space(ampm_dict.keys(), 4)
    w2 = get_table_space(ampm_dict.values(), 5)
    line = "-" * (w1 + w2 + 3)
    header = f"|" + ((w1 - 5) * " ") + "time | items" + ((w2 - 6) * " ") + "|"
    row = ""
    for i in ampm_dict:
        n = "\n"
        value = ", ".join(ampm_dict[i])
        value_len = len(value)
        row += "|" + (w1 - (len(i) + 1)) * " " + i + " | " + value + (w2 - value_len - 1) * " " + "|" + n
    row = row.rstrip("\n")
    table_list = [line, header, line, row, line]
    table_string = "\n".join(table_list)
    return table_string


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    with open(input_filename, "r") as f:
        read = f.read()
        result = create_schedule_string(read)
        output_file = open(output_filename, "w")
        output_file.write(result)


if __name__ == '__main__':
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
