import pytest
import random
from common.logger import logger


class Test_test():

    def test_test(self):
        logger.info("*************** 开始执行用例 ***************")
        list = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        randomListNum = random.randint(4, 9)
        print(randomListNum)
        randomList = random.sample(list, randomListNum)
        print(randomList)
        t = ""
        t = t.join(randomList)
        print(t)
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test.py"])
