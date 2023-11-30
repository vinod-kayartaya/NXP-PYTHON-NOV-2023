"""
Thread synchronization issues
"""
from threading import Thread, Lock
import time

lock = Lock()  # create an object of lock


def add_word(words, sentence):
    # task before acquiring the lock will be executed in a concurrent manner
    with lock:  # the following block is the `synchronized` block. other threads depending on `words`, will have to wait
        for each_word in sentence.split(' '):
            words.append(each_word)
            time.sleep(0.1)  # current thread goes into the `waiting` state
            # after waking from the sleep, it will go the `runnable` state
            # and waits for its turn to become a `running` thread
    # task after releasing the lock will be executed in a concurrent manner


def main():
    list_of_words = []  # writable resource shared by multiple threads
    s1 = 'my name is vinod and i live in bangalore'
    s2 = 'the quick brown fox jumps over the lazy dog'
    s3 = 'python is an easy to learn interpreted programming language'

    t1 = Thread(target=add_word, args=(list_of_words, s1))
    t2 = Thread(target=add_word, args=(list_of_words, s2))
    t3 = Thread(target=add_word, args=(list_of_words, s3))
    for t in (t1, t2, t3): t.start()
    for t in (t1, t2, t3): t.join()
   
    print(list_of_words)


if __name__ == '__main__':
    main()
