import sys

sys.path.append("./modules")

from sender import Sender

def main():
    g = [{'key1': 'val1'}, {'key2' : 'data2'}]
    d = Sender()
    d.post_prediction_record(g)

if __name__ == '__main__':
    main()
