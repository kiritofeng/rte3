def check(process_output, judge_output, **kwargs):
    process_lines = list(filter(None, process_output.split('\n')))
    judge_lines = list(filter(None, judge_output.split('\n')))

    if len(process_lines) != 1:
        return False

    try:
        total_cliques = sum(map(int, process_lines))
    except ValueError:
        raise Exception('Invalid output file passed!')
    try:
        return int(judge_lines[0]) == total_cliques
    except ValueError:
        return False

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print('Usage: python3 p2.py <judge_file> <your_output_file>')
        sys.exit(-1)


    judge_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(judge_file, 'rb') as jf, open(output_file, 'rb') as of:
        ret = check(jf.read(), of.read())

    sys.exit(not ret)
