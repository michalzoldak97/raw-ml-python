import csv
import random


random.seed(72502418)

d_pth = "/home/michal/Programming/Python/raw-ml/data/"

train = []
test = []


def _save_ratings_data():
    global train, test
    with open(d_pth + "train_rating.csv", "w") as trn:
        w = csv.writer(trn)
        w.writerows(train)
    
    with open(d_pth + "test_rating.csv", "w") as tst:
        w = csv.writer(tst)
        w.writerows(test)

    l_trn = len(train)
    r = l_trn / (l_trn + len(test))
    print("Train: {} Test{}".format(r, 1 - r))


def _parse_row(u: dict, row: list):
    global train, test
    new_r = (row[0], row[1], row[2])

    if row[0] not in u.keys():
        u[row[0]] = 0
        train.append(new_r)
        return

    u[row[0]] += 1
    c = random.randint(1, 10)

    if c > 8:
        test.append(new_r)
    else:
        train.append(new_r)



def split_test_train_val():
    user_cnt = {}

    with open(d_pth + "ratings.csv", "r") as r:
        r_reader = csv.reader(r)
        for row in r_reader:
            _parse_row(user_cnt, row)

    _save_ratings_data()


if __name__ == "__main__":
    split_test_train_val()
