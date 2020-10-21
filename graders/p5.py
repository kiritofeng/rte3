def utf8text(maybe_bytes, errors='strict'):
    if maybe_bytes is None:
        return None
    if isinstance(maybe_bytes, str):
        return maybe_bytes
    return maybe_bytes.decode('utf-8', errors)

def verify_relative(process_float, judge_float, epsilon):
    p1 = min(judge_float * (1 - epsilon), judge_float * (1 + epsilon))
    p2 = max(judge_float * (1 - epsilon), judge_float * (1 + epsilon))
    # Since process_float can be NaN, this is NOT equivalent to
    # (process_float < p1 or process_float > p2)
    return p1 <= process_float <= p2

def check(process_output, judge_output, **kwargs):
    EPS = 0.01 # Give 1% eps

    process_lines = list(filter(None, utf8text(process_output).split('\n')))
    judge_lines = list(filter(None, utf8text(judge_output).split('\n')))

    if len(process_lines) != len(judge_lines):
        return False

    for process_line, judge_line in zip(process_lines, judge_lines):
        try:
            k_cliques = int(judge_line)
        except ValueError:
            raise Exception('Invalid output file passed!')
        try:
            if not verify_relative(int(process_line), k_cliques, EPS):
                return False
        except ValueError:
            return False

    return True

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print('Usage: python3 p5.py <judge_file> <your_output_file>')
        sys.exit(-1)


    judge_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(judge_file, 'rb') as jf, open(output_file, 'rb') as of:
        ret = check(jf.read(), of.read())

    sys.exit(not ret)
