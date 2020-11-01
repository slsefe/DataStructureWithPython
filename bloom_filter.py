"""bloom filter
### 哈希表
- 定义：使用哈希函数将元素映射为索引，将元素存放到对应索引的位置中去。
- 哈希冲突：当多个元素对应同一个索引的时候，称为哈希冲突。
- 拉链法：当遇到哈希冲突的时候，有多种解决方法，最常用的是拉链法。拉链法将冲突的元素以链表的形式保存，将哈希表从一维结构升级为二维结构。
- 哈希表适合于存储一种映射关系，常见操作有添加删除一个元素、判断元素是否存在、获取元素的值。
- 在其它一些场景，不需要存储元素的值和额外信息，只需要判断元素是否存在，这时哈希表就有些大材小用了。
### 布隆过滤器
- 定义：布隆过滤器由一系列随机映射函数和一个二进制向量构成，用于快速检查一个元素是否在一个集合中。
- 操作：
    - 插入操作：将元素哈希取模之后对应的向量下标置为1
    - 查询元素是否存在：查询元素哈希取模之后对应的向量下标，如果有0则不存在，否则有可能存在
- 优缺点
    - 优点：时间复杂度：只需要做映射函数个数的位运算；空间复杂度：二进制向量bit数
    - 缺点：有一定的误识别率，元素删除操作困难
"""

from bitarray import bitarray
import mmh3


class BloomFilter:
    def __init__(self, size, hash_sum):
        """

        :param size: the length of bit array
        :param hash_sum: the number of hash functions
        """
        self.size = size
        self.hash_sum = hash_sum
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def add(self, s):
        for seed in range(self.hash_sum):
            index = mmh3.hash(s, seed) % self.size
            self.bit_array[index] = 1

    def lookup(self, s):
        for seed in range(self.hash_sum):
            index = mmh3.hash(s, seed) % self.size
            if self.bit_array[index] == 0:
                return "Nope"
        return "Probably"


bf = BloomFilter(500000, 7)


