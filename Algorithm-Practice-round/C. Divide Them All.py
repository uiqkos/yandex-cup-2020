fig_count = int(input())

exit_ = False

figures = []
for i in range(fig_count):
    figures.append([float(j) for j in input().split()])


if fig_count in (1, 2):
    print('Yes')


else:

    def get_center(fig):
        fig_type, *args = fig
        if fig_type == 0:
            return args[1], args[2]
        if fig_type == 1:
            # x1, y1, x2, y2, x3, y3, x4, x5 = args
            # return (x1 + x3) / 2, (y1 + y3) / 2
            return (args[0] + args[4]) / 2, (args[1] + args[5]) / 2

    def get_line(x1, y1, x2, y2):
        if x1 == x2:
            return 0, y1
        return (y2 - y1) / (x2 - x1), (-x1 * (y2 - y1)) / (x2 - x1) + y1  # return a, b where ax + b = y


    centres = list(map(lambda fig: get_center(fig), figures))

    x1, y1 = centres[0]
    x2, y2 = centres[0]

    for center in centres:
        if center != (x1, y1):
            x2, y2 = center
            break

    a, b = get_line(x1, y1, x2, y2)

    for center in centres:
        if a * center[0] + b != center[1]:  # ax + b = y
            print('No')
            exit_ = True
            break

    if not exit_:
        print('Yes')

