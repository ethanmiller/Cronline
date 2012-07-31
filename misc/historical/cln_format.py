#!/usr/bin/python
import sys, os, json, re
PATTERN_CMD = '\[[^]]+\]'
PATTERN_DT = "'[^']+'"

def main():
    log_file = sys.argv[1]
    if not os.path.exists(log_file):
        print 'no file %s' % log_file
        sys.exit(1)
    color = None
    if len(sys.argv) == 3:
        color = sys.argv[2]
    result = []
    for line in open(log_file).readlines():
        cmd = re.match(PATTERN_CMD, line).group()[1:-1]
	dates = re.findall(PATTERN_DT, line)
	start = dates[0][1:-1]
        end = dates[1][1:-1]
        res = {'start': start, 'end': end, 'description': cmd}
        if color:
            res['color'] = color
        result.append(res)
    print json.dumps(result)

if __name__ == '__main__':
    main()
