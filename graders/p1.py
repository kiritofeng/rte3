def utf8text(maybe_bytes, errors='strict'):
    if maybe_bytes is None:
        return None
    if isinstance(maybe_bytes, str):
        return maybe_bytes
    return maybe_bytes.decode('utf-8', errors)

def check(process_output, judge_output, **kwargs):
    process_lines = list(filter(None, utf8text(process_output).split('\n')))
    judge_lines = list(filter(None, utf8text(judge_output).split('\n')))

    if len(process_lines) != 1:
        return False

    try:
        three_cliques = int(judge_lines[0]) if judge_lines else 0
    except ValueError:
        raise Exception('Invalid output file passed!')
    try:
        return int(process_lines[0]) == three_cliques
        if int(process_lines[0]) == three_cliques:
            return True
    except ValueError:
        return False

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print('Usage: python3 p1.py <judge_file> <your_output_file>')
        sys.exit(-1)


    judge_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(judge_file, 'rb') as jf, open(output_file, 'rb') as of:
        ret = check(jf.read(), of.read())

    sys.exit(not ret)
