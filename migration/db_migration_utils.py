import time

class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))


class DbMigrationUtils():
    def save_rows(self, filename, rows):
        file = open(filename, 'w', encoding='UTF-8')
        for item in rows:
            row = ";".join(["%s=%s" % (k, v) for k, v in item.items()])
            file.write(row)
            file.write('\n')
