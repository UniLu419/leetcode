# 复习索引

由 `python3 lc.py index` 根据各题 notes.md 生成，改笔记后重新运行即可。

## 双指针（15）

- [5. Longest Palindromic Substring](problems/0005_longest_palindromic_substring/notes.md)
  - 识别信号：求最长的回文连续子串：回文关于中心对称，从中心向两边扩展就能枚举出所有回文；len(s) ≤ 1000，O(n²) 可以接受
  - 关键一步：以每个字符、以及每两个相邻字符之间为中心，左右指针同时向外扩展，字符相等就继续；奇数长度和偶数长度的回文要分别枚举中心。
- [11. Container With Most Water](problems/0011_container_with_most_water/notes.md)
  - 识别信号：在数组里选两条线，面积 = min(两条线的高) × 下标距离，求最大值；从两端向中间收缩时宽度一定变小，只有更高的边才可能让面积变大
  - 关键一步：面积受较矮的一边限制；较矮的一边和更靠里的任何线组成的容器都不会更大，所以可以直接舍弃它，把这一侧的指针往里移。
- [15. 3Sum](problems/0015_3sum/notes.md)
  - 识别信号：找出所有和为 0 的三元组，且结果不能有重复的三元组：排序后相同的数挨在一起，方便去重；固定一个数后，剩下的就是"在有序数组里找两数之和等于目标值"，可以用左右双指针
  - 关键一步：排序后固定 nums[i]，在它右侧用左右双指针找两数之和等于 −nums[i]；三个位置都跳过相同的值，结果就不会重复。
- [21. Merge Two Sorted Lists](problems/0021_merge_two_sorted_lists/notes.md)
  - 识别信号：把两个已经升序的链表合成一个升序链表，就是归并排序里的合并步骤；要求拼接原有节点，不需要新建节点
  - 关键一步：每次比较两条链表的当前节点，把较小的接到结果尾部；一条链表走完后，另一条的剩余部分直接整段接上。
- [26. Remove Duplicates from Sorted Array](problems/0026_remove_duplicates_from_sorted_array/notes.md)
  - 识别信号：数组已经按非递减排序，要求原地去重；返回保留下来的个数 k，只检查前 k 个元素；要求 O(1) 额外空间
  - 关键一步：数组有序，所以新出现的值一定比已保留部分的最后一个值大，只需比较 nums[i] 和 nums[k]。
- [27. Remove Element](problems/0027_remove_element/notes.md)
  - 识别信号：原地删除所有等于 val 的元素，返回剩下的个数 k；只检查前 k 个元素，顺序可以改变，后面的内容不用管
  - 关键一步：不等于 val 的元素依次覆盖到 nums[i]，遍历结束时 i 就是保留的个数。
- [42. Trapping Rain Water](problems/0042_trapping_rain_water/notes.md)
  - 识别信号：每个位置的答案 = min(左边最高, 右边最高) − 自身高度，即由"左右两侧的最大值"共同决定；原注释：这类需要计算左右最大高度的最小值的题，第一反应是从左到右取最大值，再从右到左取最大值，然后比较两者最小值，往往可以简化为维护单方向最大值，根据具体情况判断左右处理顺序
  - 关键一步：左右指针哪边当前高度更低就处理哪边：另一侧已经有一块不低于它的挡板，所以这个位置的水位只取决于它这一侧的最大值。
- [80. Remove Duplicates from Sorted Array II](problems/0080_remove_duplicates_from_sorted_array_ii/notes.md)
  - 识别信号：有序数组、原地删除、只允许 O(1) 额外空间，返回保留的个数 k；每个值最多保留两个，是否保留只和"已保留部分"的末尾有关
  - 关键一步：数组有序，只要 nums[i] 不等于已保留部分的倒数第二个元素，保留它就不会出现三个相同的数。
- [88. Merge Sorted Array](problems/0088_merge_sorted_array/notes.md)
  - 识别信号：两个有序数组合并，结果要原地写进 nums1；nums1 尾部预留了 n 个空位
  - 关键一步：从后往前填：nums1 尾部的空位足够放下所有较大的元素，写指针永远不会越过 nums1 的读指针，不会覆盖未读元素。
- [125. Valid Palindrome](problems/0125_valid_palindrome/notes.md)
  - 识别信号：判断回文，但要先忽略大小写、只保留字母和数字；回文判断天然是首尾两端向中间对比
  - 关键一步：左右指针各自先跳过非字母数字字符，再比较两个字符的小写形式。
- [151. Reverse Words in a String](problems/0151_reverse_words_in_a_string/notes.md)
  - 识别信号：以单词为单位反转顺序，同时要去掉首尾空格、把单词间的多个空格压成一个；进阶：字符串可变时要求 O(1) 额外空间，提示"整体反转 + 每个单词再反转"
  - 关键一步：不带参数的 split() 一步解决首尾空格和连续空格，剩下只是把单词顺序反过来。
- [167. Two Sum II - Input Array Is Sorted](problems/0167_two_sum_ii_input_array_is_sorted/notes.md)
  - 识别信号：数组已按非递减顺序排好，找两个数之和等于 target；要求只用常数额外空间，提示不用哈希表、改用有序性
  - 关键一步：和小于 target 时，numbers[l] 与剩下任何一个数相加都不会超过当前的和，所以 l 可以直接排除；和大于 target 时同理排除 r。
- [189. Rotate Array](problems/0189_rotate_array/notes.md)
  - 识别信号：数组原地向右轮转 k 步，进阶要求 O(1) 额外空间；k 可能大于数组长度，需要先对长度取模
  - 关键一步：整体反转后，原来的后 k 个元素到了前面但顺序是反的，前 k 个和后 n − k 个各自再反转一次就恢复了顺序。
- [228. Summary Ranges](problems/0228_summary_ranges/notes.md)
  - 识别信号：有序、无重复的整数数组，把连续的数合并成区间；输出每段连续区间的起点和终点
  - 关键一步：比较 nums[j] + 1 == nums[j + 1]，决定是延伸当前段还是新开一段。
- [392. Is Subsequence](problems/0392_is_subsequence/notes.md)
  - 识别信号：判断 s 是否是 t 的子序列：字符相对顺序要保持，但不要求连续；两个序列各自单向前进、互相匹配，适合两个指针同步扫描
  - 关键一步：贪心匹配：s 的每个字符都和 t 中能匹配的最早位置配对，配上就移动 s 的指针。

## 哈希表（15）

- [1. Two Sum](problems/0001_two_sum/notes.md)
  - 识别信号：在数组里找"两个数之和等于 target"，并且要返回下标（排序会打乱原位置）；换个说法：对每个数，查"target − 它"有没有出现过
  - 关键一步：遍历到 nums[i] 时，先查 target − nums[i] 是否已在哈希表里；查不到再把 nums[i] 存进去。
- [3. Longest Substring Without Repeating Characters](problems/0003_longest_substring_without_repeating_characters/notes.md)
  - 识别信号：求满足条件（无重复字符）的"最长连续子串"；右端加入一个字符时，只需看这个字符是否已经在窗口里，可以 O(1) 判断
  - 关键一步：哈希表记录每个字符最后出现的下标；遇到重复字符时，只有它上次出现的位置还在窗口内（≥ l）才把左端移到该位置 + 1，左端只往右走。
- [13. Roman to Integer](problems/0013_roman_to_integer/notes.md)
  - 识别信号：按固定的符号表把字符串翻译成数值；"小数在大数左边表示相减"只有 6 种组合：IV、IX、XL、XC、CD、CM
  - 关键一步：先看当前位置和下一个位置组成的两个字符是否在表里（减法组合），在就整体加上并跳两格，不在就只加当前字符。
- [36. Valid Sudoku](problems/0036_valid_sudoku/notes.md)
  - 识别信号：只判断已填数字在每行、每列、每个 3×3 宫内不重复，不要求数独能解；判重 → 哈希表 / 集合；棋盘固定 9×9
  - 关键一步：用宫号公式 (i // 3)·3 + j // 3 把格子归到所在的 3×3 宫，这样行、列、宫的判重可以在同一遍扫描里完成。
- [49. Group Anagrams](problems/0049_group_anagrams/notes.md)
  - 识别信号：把"字母相同、顺序不同"的字符串分到同一组；分组 → 给每组找一个相同的、可哈希的"签名"做字典键
  - 关键一步：把"互为异位词"转成"签名相同"：签名必须可哈希，排序后的字符串或计数元组都可以，dict 不行。
- [73. Set Matrix Zeroes](problems/0073_set_matrix_zeroes/notes.md)
  - 识别信号：原地修改矩阵，某个格子是 0 会影响它所在的整行和整列；边扫边改会让新写入的 0 继续"传染"，必须先记录、后修改
  - 关键一步：分两遍：先标记含 0 的行和列，再清零；O(1) 空间版本把这些标记存在第一行和第一列里。
- [128. Longest Consecutive Sequence](problems/0128_longest_consecutive_sequence/notes.md)
  - 识别信号：数组未排序，求值连续的最长序列长度（不要求在原数组中相邻）；题目要求 O(n) 时间，排除了排序，提示用哈希集合 O(1) 查"x+1 在不在"
  - 关键一步：只从 x − 1 不在集合中的 x 开始向上延伸，这样每个连续段只被完整扫描一次。
- [138. Copy List with Random Pointer](problems/0138_copy_list_with_random_pointer/notes.md)
  - 识别信号：深拷贝一个带 random 指针的链表，新链表不能指向原链表的任何节点；random 可能指向后面还没复制的节点，需要"原节点 → 新节点"的对应关系
  - 关键一步：先建立"原节点 → 新节点"的映射，再统一连 random，这样 random 指向的节点一定已经存在。
- [141. Linked List Cycle](problems/0141_linked_list_cycle/notes.md)
  - 识别信号：判断链表是否有环；进阶要求 O(1) 额外空间，提示快慢指针
  - 关键一步：快指针每步比慢指针多走 1 步，进环后两者距离每步缩小 1，一定会相遇。
- [202. Happy Number](problems/0202_happy_number/notes.md)
  - 识别信号：反复做同一个变换，结果要么到达 1，要么无限循环；判断"是否进入循环"：记录见过的值，或者用快慢指针判环
  - 关键一步：平方和序列只能到 1 或进入循环，问题等价于判环：见过的数再次出现，就不是快乐数。
- [205. Isomorphic Strings](problems/0205_isomorphic_strings/notes.md)
  - 识别信号：两个字符串逐位置对应，判断能否在字符之间建立映射；"不同字符不能映射到同一个字符"，说明映射必须是一一对应
  - 关键一步：只记 s → t 不够，还要记 t → s：s 里一个新字符想映射到的 t 字符如果已经被别的字符占用，就不同构（"badc" 和 "baba"）。
- [219. Contains Duplicate II](problems/0219_contains_duplicate_ii/notes.md)
  - 识别信号：判断是否存在两个相等的元素，且下标差 ≤ k；"距离不超过 k"：只关心每个值上一次出现的位置，或者维护长度为 k 的窗口
  - 关键一步：对同一个值，最近一次出现离当前位置最近；它都超过 k，更早的只会更远。
- [290. Word Pattern](problems/0290_word_pattern/notes.md)
  - 识别信号：pattern 的字母和 s 的单词之间要"一一对应"（双射）：同一字母只能对应同一单词，不同字母不能对应同一单词；需要记录"已经见过的映射"，并能 O(1) 反查
  - 关键一步：双射要两个方向都检查：新单词第一次出现时，它要对应的字母必须还没被别的单词占用。
- [380. Insert Delete GetRandom O(1)](problems/0380_insert_delete_getrandom_o_1/notes.md)
  - 识别信号：要求 insert、remove、getRandom 都是平均 O(1)；哈希表能 O(1) 增删查，但不能 O(1) 等概率随机取；数组能 O(1) 随机取，但不能 O(1) 删除中间元素，需要把两者结合
  - 关键一步：删除中间元素时，用数组末尾元素覆盖被删位置、更新末尾元素在哈希表里的下标，再 pop 末尾，避免数组整体移位。
- [Booking: Award Top K Hotels](problems/booking_award_topk_hotels/notes.md)
  - 识别信号：题目（HackerRank，Booking 面试题）：给出正面关键词串 positiveKeywords、负面关键词串 negativeKeywords（空格分隔），以及等长的 hotelIds 和 reviews（第 i 条评论属于 hotelIds[i]）。评论中每出现一次正面词加 3 分、负面词减 1 分；匹配不区分大小写，单词按空白切分并去掉首尾的 . , ! ?。同一酒店的分数累加，返回得分最高的 k 个酒店 id，同分按 id 升序；不足 k 个就全部返回；"按某个 key 累加分数"用哈希表，"取前 k 名、多关键字排序"用排序（或大小为 k 的堆）
  - 关键一步：排序键写成 (−分数, id)：分数降序、同分时 id 升序一次完成。

## 字符串模拟（13）

- [6. Zigzag Conversion](problems/0006_zigzag_conversion/notes.md)
  - 识别信号：按固定规则把字符"摆"成图形，再按行读出，属于模拟；摆放是周期性的：竖着向下 numRows 个、斜着向上 numRows − 2 个，可以用取余直接算出每个字符落在哪一行
  - 关键一步：周期 step = 2·numRows − 2；余数 r = i mod step，r < numRows 时行号是 r，否则行号是 step − r。
- [12. Integer to Roman](problems/0012_integer_to_roman/notes.md)
  - 识别信号：把一个数拆成固定"面额"的组合，每次取能用的最大面额，类似找零钱；1 ≤ num ≤ 3999，面额只有固定的 13 项（7 个单字符加 4、9、40、90、400、900 六个减法形式）
  - 关键一步：把 CM、CD、XC、XL、IX、IV 六个减法形式也放进面额表，从大到小贪心地减，结果自动符合罗马数字的书写规则。
- [13. Roman to Integer](problems/0013_roman_to_integer/notes.md)
  - 识别信号：按固定的符号表把字符串翻译成数值；"小数在大数左边表示相减"只有 6 种组合：IV、IX、XL、XC、CD、CM
  - 关键一步：先看当前位置和下一个位置组成的两个字符是否在表里（减法组合），在就整体加上并跳两格，不在就只加当前字符。
- [14. Longest Common Prefix](problems/0014_longest_common_prefix/notes.md)
  - 识别信号：求所有字符串共同的前缀：前缀长度不会超过最短的字符串；可以按列（同一个下标）比较所有字符串，遇到第一个不一致就停
  - 关键一步：前缀长度以最短字符串为上限；按列逐位比较所有字符串，第一个不一致的位置就是前缀的终点。
- [28. Find the Index of the First Occurrence in a String](problems/0028_find_the_index_of_the_first_occurrence_in_a_string/notes.md)
  - 识别信号：在主串里找模式串第一次出现的位置，找不到返回 -1；只有两个字符串、没有其他条件，就是标准的字符串匹配
  - 关键一步：失配时利用 needle 已匹配部分的最长相等前后缀，直接把模式串对齐过去继续比较，主串指针不回头。
- [58. Length of Last Word](problems/0058_length_of_last_word/notes.md)
  - 识别信号：只关心字符串末尾的一段（最后一个单词）；单词之间、首尾都可能有多个空格
  - 关键一步：从右往左扫：跳过尾部空格后开始计数，碰到下一个空格立即停止。
- [67. Add Binary](problems/0067_add_binary/notes.md)
  - 识别信号：两个二进制字符串相加，长度可达 10^4，不能指望转成固定宽度的整数（其他语言会溢出）；逐位相加加进位，和竖式加法一样
  - 关键一步：每一位的和 = a 位 ⊕ b 位 ⊕ 进位，新进位 = 三者中至少两个为 1；从右往左一遍扫完。
- [68. Text Justification](problems/0068_text_justification/notes.md)
  - 识别信号：每行尽可能多放单词（贪心装行）；空格分配有精确规则：尽量平均，多出来的从左往右分；最后一行和只有一个单词的行左对齐
  - 关键一步：q, r = divmod(总空格数, 空位数)：每个空位 q 个空格，左边 r 个空位各多 1 个。
- [71. Simplify Path](problems/0071_simplify_path/notes.md)
  - 识别信号：".." 表示回到上一级，要撤销"最近一次进入的目录"，后进先出；路径按 "/" 分段后，每一段独立处理
  - 关键一步：用栈保存目录名，".." 就弹出栈顶；在根目录时栈为空，".." 什么也不做。
- [125. Valid Palindrome](problems/0125_valid_palindrome/notes.md)
  - 识别信号：判断回文，但要先忽略大小写、只保留字母和数字；回文判断天然是首尾两端向中间对比
  - 关键一步：左右指针各自先跳过非字母数字字符，再比较两个字符的小写形式。
- [151. Reverse Words in a String](problems/0151_reverse_words_in_a_string/notes.md)
  - 识别信号：以单词为单位反转顺序，同时要去掉首尾空格、把单词间的多个空格压成一个；进阶：字符串可变时要求 O(1) 额外空间，提示"整体反转 + 每个单词再反转"
  - 关键一步：不带参数的 split() 一步解决首尾空格和连续空格，剩下只是把单词顺序反过来。
- [224. Basic Calculator](problems/0224_basic_calculator/notes.md)
  - 识别信号：只含 +、−、括号、空格和非负整数的表达式求值，不能用 eval；括号可以嵌套，要用栈保存进入括号前的状态
  - 关键一步：每个数最终的正负号 = 它前面运算符的符号 × 外层所有括号的整体符号，栈顶 sign_stack[-1] 就是外层括号的累计符号。
- [Booking: Shift Strings](problems/booking_shift_strings/notes.md)
  - 识别信号：题目（HackerRank，Booking 面试题）：一次左移把首字符移到末尾，一次右移把末字符移到开头。对字符串 s 先做 leftShifts 次左移、再做 rightShifts 次右移，返回结果；左移和右移互相抵消，移动 len(s) 次回到原样，用取模算净位移
  - 关键一步：把所有移位合成一次净左移 (leftShifts − rightShifts) mod n，再切片拼接。

## 贪心（10）

- [11. Container With Most Water](problems/0011_container_with_most_water/notes.md)
  - 识别信号：在数组里选两条线，面积 = min(两条线的高) × 下标距离，求最大值；从两端向中间收缩时宽度一定变小，只有更高的边才可能让面积变大
  - 关键一步：面积受较矮的一边限制；较矮的一边和更靠里的任何线组成的容器都不会更大，所以可以直接舍弃它，把这一侧的指针往里移。
- [12. Integer to Roman](problems/0012_integer_to_roman/notes.md)
  - 识别信号：把一个数拆成固定"面额"的组合，每次取能用的最大面额，类似找零钱；1 ≤ num ≤ 3999，面额只有固定的 13 项（7 个单字符加 4、9、40、90、400、900 六个减法形式）
  - 关键一步：把 CM、CD、XC、XL、IX、IV 六个减法形式也放进面额表，从大到小贪心地减，结果自动符合罗马数字的书写规则。
- [45. Jump Game II](problems/0045_jump_game_ii/notes.md)
  - 识别信号：nums[i] 是从 i 最多能跳的距离，求到达最后一个位置的最少跳跃次数；保证能到达终点；求"最少步数" → 按步数分层（BFS），而每一层都是一段连续区间
  - 关键一步：第 s 步能到达的位置是连续的一段，扫到这一段的右边界 end 时必须再跳一次，新的右边界就是这一段里能跳到的最远位置 max_len。
- [55. Jump Game](problems/0055_jump_game/notes.md)
  - 识别信号：nums[i] 是从 i 最多能跳的距离，问能否到达最后一个位置；只问"能不能到"，不问步数 → 只需要维护最远可达位置
  - 关键一步：能到达的下标总是连续的一段 [0, farthest]，所以只需要维护 farthest 一个数。
- [68. Text Justification](problems/0068_text_justification/notes.md)
  - 识别信号：每行尽可能多放单词（贪心装行）；空格分配有精确规则：尽量平均，多出来的从左往右分；最后一行和只有一个单词的行左对齐
  - 关键一步：q, r = divmod(总空格数, 空位数)：每个空位 q 个空格，左边 r 个空位各多 1 个。
- [122. Best Time to Buy and Sell Stock II](problems/0122_best_time_to_buy_and_sell_stock_ii/notes.md)
  - 识别信号：可以买卖任意多次，但同一时间最多持有一股；任意一段上涨都可以拆成相邻两天的上涨之和
  - 关键一步：总利润 = 所有相邻两天正差价之和。
- [134. Gas Station](problems/0134_gas_station/notes.md)
  - 识别信号：环形路线，从某个起点出发油量全程不能为负，求起点；题目保证有解时解唯一；总油量 ≥ 总消耗是有解的充要条件
  - 关键一步：从 start 出发到 i 时累计油量为负，则 start 到 i 之间都不能当起点，直接把起点跳到 i + 1。
- [135. Candy](problems/0135_candy/notes.md)
  - 识别信号：每人至少 1 颗，评分比相邻高的要比相邻的多，求最少总数；约束同时来自左邻居和右邻居，可以拆成"只看左边"和"只看右边"两个方向分别满足
  - 关键一步：左右各扫一遍：第二遍只在"评分高于右邻且糖果不多于右邻"时改成右邻 + 1，这等价于取两个方向要求的最大值。
- [452. Minimum Number of Arrows to Burst Balloons](problems/0452_minimum_number_of_arrows_to_burst_balloons/notes.md)
  - 识别信号：一组区间，用最少的"点"覆盖所有区间（一支箭就是一个 x 坐标）；端点相接也算重叠（x_start ≤ x ≤ x_end）
  - 关键一步：按起点排序后，当前组的交集右端是 min(各终点)；新气球起点 ≤ 这个右端就能共用一支箭，否则必须再射一支。
- [Booking: Minimum Sum](problems/booking_minimum_sum/notes.md)
  - 识别信号：题目（HackerRank，Booking 面试题）：给定整数数组 num 和整数 k，执行恰好 k 次操作，每次选一个元素 x 替换成 ceil(x / 2)，返回 k 次操作后数组之和的最小可能值；每次都要取"当前最大值"并把变小的值放回去，是典型的最大堆场景
  - 关键一步：每次操作都作用在当前最大值上，用最大堆维护"当前最大"。

## 链表（10）

- [2. Add Two Numbers](problems/0002_add_two_numbers/notes.md)
  - 识别信号：两个非负整数按"逆序"存在链表里，个位在表头，正好可以从头开始逐位相加；返回同样格式的链表，结果最多比较长的链表多 1 位（最高位进位）
  - 关键一步：每一位的结果是 (a + b + 进位) 的个位，新进位是它整除 10；两条链表都走完后进位不为 0 还要补一个节点。
- [19. Remove Nth Node From End of List](problems/0019_remove_nth_node_from_end_of_list/notes.md)
  - 识别信号：要删"倒数第 n 个"节点，而单链表只能从头往后走；进阶要求只遍历一次：让一个指针比另一个固定落后 n 步
  - 关键一步：后面的指针始终比前面的指针落后 n 步，停在待删节点的前驱；前面的指针走完时执行 前驱.next = 前驱.next.next。
- [21. Merge Two Sorted Lists](problems/0021_merge_two_sorted_lists/notes.md)
  - 识别信号：把两个已经升序的链表合成一个升序链表，就是归并排序里的合并步骤；要求拼接原有节点，不需要新建节点
  - 关键一步：每次比较两条链表的当前节点，把较小的接到结果尾部；一条链表走完后，另一条的剩余部分直接整段接上。
- [25. Reverse Nodes in k-Group](problems/0025_reverse_nodes_in_k_group/notes.md)
  - 识别信号：链表"每 k 个节点一组翻转"，最后不足 k 个的保持原顺序；要求交换节点本身而不是改节点的值；进阶要求 O(1) 额外空间
  - 关键一步：每组先确认够 k 个再反转；反转后把上一组的尾巴接到本组的新头，本组的新尾巴（原来的组头）接到下一组的开头。
- [61. Rotate List](problems/0061_rotate_list/notes.md)
  - 识别信号：链表整体向右旋转 k 位，等价于把末尾 k 个节点整体搬到头部；k 可能远大于链表长度（k ≤ 2·10^9）
  - 关键一步：先 k %= n，新头是第 n − k 个节点的下一个节点：首尾相连成环后，在第 n − k 个节点处断开。
- [82. Remove Duplicates from Sorted List II](problems/0082_remove_duplicates_from_sorted_list_ii/notes.md)
  - 识别信号：有序链表，出现重复的数字要一个不留地全部删除；头节点本身也可能被删，"新头"在扫描前不确定
  - 关键一步：有序意味着重复值相邻：发现 head.val == head.next.val 就把这一整段跳过，只有和后一个不同的节点才接到结果尾部。
- [83. Remove Duplicates from Sorted List](problems/0083_remove_duplicates_from_sorted_list/notes.md)
  - 识别信号：有序链表，重复值一定相邻；每个值保留一个，所以头节点永远不会被删
  - 关键一步：删掉下一个节点后先不前进，继续和新的下一个节点比较，这样连续多个重复都能删掉。
- [92. Reverse Linked List II](problems/0092_reverse_linked_list_ii/notes.md)
  - 识别信号：只反转链表中位置 left 到 right 的一段，其余部分保持原样；进阶要求一趟扫描完成
  - 关键一步：头插法：pre 和 cur 固定不动，每次把 cur 后面的节点移到 pre 后面，right − left 次之后这一段就反转了。
- [138. Copy List with Random Pointer](problems/0138_copy_list_with_random_pointer/notes.md)
  - 识别信号：深拷贝一个带 random 指针的链表，新链表不能指向原链表的任何节点；random 可能指向后面还没复制的节点，需要"原节点 → 新节点"的对应关系
  - 关键一步：先建立"原节点 → 新节点"的映射，再统一连 random，这样 random 指向的节点一定已经存在。
- [141. Linked List Cycle](problems/0141_linked_list_cycle/notes.md)
  - 识别信号：判断链表是否有环；进阶要求 O(1) 额外空间，提示快慢指针
  - 关键一步：快指针每步比慢指针多走 1 步，进环后两者距离每步缩小 1，一定会相遇。

## 排序（9）

- [15. 3Sum](problems/0015_3sum/notes.md)
  - 识别信号：找出所有和为 0 的三元组，且结果不能有重复的三元组：排序后相同的数挨在一起，方便去重；固定一个数后，剩下的就是"在有序数组里找两数之和等于目标值"，可以用左右双指针
  - 关键一步：排序后固定 nums[i]，在它右侧用左右双指针找两数之和等于 −nums[i]；三个位置都跳过相同的值，结果就不会重复。
- [49. Group Anagrams](problems/0049_group_anagrams/notes.md)
  - 识别信号：把"字母相同、顺序不同"的字符串分到同一组；分组 → 给每组找一个相同的、可哈希的"签名"做字典键
  - 关键一步：把"互为异位词"转成"签名相同"：签名必须可哈希，排序后的字符串或计数元组都可以，dict 不行。
- [56. Merge Intervals](problems/0056_merge_intervals/notes.md)
  - 识别信号：给一组区间，合并所有重叠的区间；输入无序；排序后，能合并的区间会相邻
  - 关键一步：按起点排序后，只需要和结果的最后一个区间比较。
- [128. Longest Consecutive Sequence](problems/0128_longest_consecutive_sequence/notes.md)
  - 识别信号：数组未排序，求值连续的最长序列长度（不要求在原数组中相邻）；题目要求 O(n) 时间，排除了排序，提示用哈希集合 O(1) 查"x+1 在不在"
  - 关键一步：只从 x − 1 不在集合中的 x 开始向上延伸，这样每个连续段只被完整扫描一次。
- [169. Majority Element](problems/0169_majority_element/notes.md)
  - 识别信号：多数元素的出现次数严格大于 n / 2，并且保证存在；进阶要求 O(n) 时间、O(1) 空间
  - 关键一步：多数元素超过一半，和其他元素两两抵消后剩下的一定是它；排序版本里，它的连续段一定覆盖下标 n // 2。
- [274. H-Index](problems/0274_h_index/notes.md)
  - 识别信号：求最大的 h，使"至少有 h 个数 ≥ h"，答案随排序后的位置单调变化；h 不会超过数组长度 n，引用数大于 n 的都可以当作 n 处理（可以按次数分桶计数）
  - 关键一步：降序排序后，citations[i] ≥ i + 1 等价于"前 i + 1 篇的引用都至少是 i + 1"，所以 h 就是满足这个条件的最大 i + 1。
- [452. Minimum Number of Arrows to Burst Balloons](problems/0452_minimum_number_of_arrows_to_burst_balloons/notes.md)
  - 识别信号：一组区间，用最少的"点"覆盖所有区间（一支箭就是一个 x 坐标）；端点相接也算重叠（x_start ≤ x ≤ x_end）
  - 关键一步：按起点排序后，当前组的交集右端是 min(各终点)；新气球起点 ≤ 这个右端就能共用一支箭，否则必须再射一支。
- [2146. K Highest Ranked Items Within a Price Range](problems/2146_k_highest_ranked_items_within_a_price_range/notes.md)
  - 识别信号：网格里有墙（0）、空地（1）、商品（价格），每步上下左右走一格，排名第一关键字是"从起点出发的最短步数"；每步代价都是 1 的最短路，就是从起点做 BFS；排名规则是多关键字（距离、价格、行、列），收集后按元组排序
  - 关键一步：BFS 按层扩展天然按距离从小到大收集商品；某一层处理完时已收集够 k 个，就不必再往外走，剩下只需按 (距离, 价格, 行, 列) 排序。
- [Booking: Award Top K Hotels](problems/booking_award_topk_hotels/notes.md)
  - 识别信号：题目（HackerRank，Booking 面试题）：给出正面关键词串 positiveKeywords、负面关键词串 negativeKeywords（空格分隔），以及等长的 hotelIds 和 reviews（第 i 条评论属于 hotelIds[i]）。评论中每出现一次正面词加 3 分、负面词减 1 分；匹配不区分大小写，单词按空白切分并去掉首尾的 . , ! ?。同一酒店的分数累加，返回得分最高的 k 个酒店 id，同分按 id 升序；不足 k 个就全部返回；"按某个 key 累加分数"用哈希表，"取前 k 名、多关键字排序"用排序（或大小为 k 的堆）
  - 关键一步：排序键写成 (−分数, id)：分数降序、同分时 id 升序一次完成。

## 数学（7）

- [2. Add Two Numbers](problems/0002_add_two_numbers/notes.md)
  - 识别信号：两个非负整数按"逆序"存在链表里，个位在表头，正好可以从头开始逐位相加；返回同样格式的链表，结果最多比较长的链表多 1 位（最高位进位）
  - 关键一步：每一位的结果是 (a + b + 进位) 的个位，新进位是它整除 10；两条链表都走完后进位不为 0 还要补一个节点。
- [6. Zigzag Conversion](problems/0006_zigzag_conversion/notes.md)
  - 识别信号：按固定规则把字符"摆"成图形，再按行读出，属于模拟；摆放是周期性的：竖着向下 numRows 个、斜着向上 numRows − 2 个，可以用取余直接算出每个字符落在哪一行
  - 关键一步：周期 step = 2·numRows − 2；余数 r = i mod step，r < numRows 时行号是 r，否则行号是 step − r。
- [7. Reverse Integer](problems/0007_reverse_integer/notes.md)
  - 识别信号：按十进制位反转一个整数：反复用 x % 10 取末位、x / 10 去掉末位；结果超出 32 位有符号整数范围要返回 0，且题目假设不能存 64 位整数，溢出必须在计算之前判断
  - 关键一步：执行 rev = rev × 10 + pop 之前，先拿 rev 和 INT_MAX / 10（负数用 INT_MIN / 10）比较，相等时再看末位是否超过 7（负数是低于 −8）。
- [9. Palindrome Number](problems/0009_palindrome_number/notes.md)
  - 识别信号：判断一个整数正读和反读是否相同；进阶要求"不转成字符串"，就只能用 % 10 和 // 10 逐位处理
  - 关键一步：负数直接返回 False；非负数用 % 10 逐位取末位拼出反转数，最后和原数比较。
- [66. Plus One](problems/0066_plus_one/notes.md)
  - 识别信号：用数组逐位存一个大整数，对它做加法，需要处理进位；最高位进位时数组长度会加 1
  - 关键一步：从末位往前，遇到不是 9 的位加 1 后立即返回；只有全部为 9 时才需要在开头补 1。
- [69. Sqrt(x)](problems/0069_sqrt_x/notes.md)
  - 识别信号：求满足 k² ≤ x 的最大整数 k，而 k² 随 k 单调递增；不允许使用内置的开方或幂运算；x 最大到 2^31 − 1
  - 关键一步：k² ≤ x 对 k 单调，二分找最后一个满足的 k；牛顿迭代则用切线逼近 √x，整数部分稳定后即为答案。
- [Booking: Shift Strings](problems/booking_shift_strings/notes.md)
  - 识别信号：题目（HackerRank，Booking 面试题）：一次左移把首字符移到末尾，一次右移把末字符移到开头。对字符串 s 先做 leftShifts 次左移、再做 rightShifts 次右移，返回结果；左移和右移互相抵消，移动 len(s) 次回到原样，用取模算净位移
  - 关键一步：把所有移位合成一次净左移 (leftShifts − rightShifts) mod n，再切片拼接。

## 栈（7）

- [20. Valid Parentheses](problems/0020_valid_parentheses/notes.md)
  - 识别信号：括号必须按正确顺序闭合：最后打开的必须最先关闭，正是后进先出；字符只有三种括号的左、右两种形式
  - 关键一步：右括号必须和栈顶的左括号配对；扫描结束时栈为空才有效。
- [25. Reverse Nodes in k-Group](problems/0025_reverse_nodes_in_k_group/notes.md)
  - 识别信号：链表"每 k 个节点一组翻转"，最后不足 k 个的保持原顺序；要求交换节点本身而不是改节点的值；进阶要求 O(1) 额外空间
  - 关键一步：每组先确认够 k 个再反转；反转后把上一组的尾巴接到本组的新头，本组的新尾巴（原来的组头）接到下一组的开头。
- [71. Simplify Path](problems/0071_simplify_path/notes.md)
  - 识别信号：".." 表示回到上一级，要撤销"最近一次进入的目录"，后进先出；路径按 "/" 分段后，每一段独立处理
  - 关键一步：用栈保存目录名，".." 就弹出栈顶；在根目录时栈为空，".." 什么也不做。
- [94. Binary Tree Inorder Traversal](problems/0094_binary_tree_inorder_traversal/notes.md)
  - 识别信号：要求按"左子树 → 根 → 右子树"的顺序输出节点值；进阶要求不用递归，提示要用显式栈模拟递归
  - 关键一步：中序就是"一路向左走到底，回来时记录当前节点，再去右子树"；递归和栈写法都只是在实现这个顺序。
- [150. Evaluate Reverse Polish Notation](problems/0150_evaluate_reverse_polish_notation/notes.md)
  - 识别信号：逆波兰表达式（后缀表达式）：每个运算符作用于它前面最近的两个操作数；"最近出现的先被使用"，是后进先出的结构
  - 关键一步：遇到运算符时，先弹出的是右操作数 b，后弹出的是左操作数 a，计算 a op b 后压回栈。
- [155. Min Stack](problems/0155_min_stack/notes.md)
  - 识别信号：设计一个栈，push、pop、top、getMin 都要 O(1)；pop 之后最小值要"回退"到之前的状态，所以每个栈状态都要记住当时的最小值
  - 关键一步：push 时往 min_stack 压入 min(val, 当前最小值)，pop 时两个栈一起弹出，弹出后 min_stack 栈顶自动回到上一个状态的最小值。
- [224. Basic Calculator](problems/0224_basic_calculator/notes.md)
  - 识别信号：只含 +、−、括号、空格和非负整数的表达式求值，不能用 eval；括号可以嵌套，要用栈保存进入括号前的状态
  - 关键一步：每个数最终的正负号 = 它前面运算符的符号 × 外层所有括号的整体符号，栈顶 sign_stack[-1] 就是外层括号的累计符号。

## 二叉树（6）

- [94. Binary Tree Inorder Traversal](problems/0094_binary_tree_inorder_traversal/notes.md)
  - 识别信号：要求按"左子树 → 根 → 右子树"的顺序输出节点值；进阶要求不用递归，提示要用显式栈模拟递归
  - 关键一步：中序就是"一路向左走到底，回来时记录当前节点，再去右子树"；递归和栈写法都只是在实现这个顺序。
- [100. Same Tree](problems/0100_same_tree/notes.md)
  - 识别信号：判断两棵树结构和节点值是否完全相同；结论可以拆成"根相同 且 左子树相同 且 右子树相同"
  - 关键一步：先处理"两个都空"和"只有一个空"这两种情况，剩下的就是值比较加左右递归。
- [101. Symmetric Tree](problems/0101_symmetric_tree/notes.md)
  - 识别信号：判断树是否是自身的镜像，也就是左子树和右子树互为镜像；进阶要求递归和迭代两种写法
  - 关键一步：比较的是成对的节点：左边的左孩子对右边的右孩子，左边的右孩子对右边的左孩子。
- [104. Maximum Depth of Binary Tree](problems/0104_maximum_depth_of_binary_tree/notes.md)
  - 识别信号：求根到最远叶子的节点数；整棵树的答案可以由左右子树的答案合成：max(左深度, 右深度) + 1
  - 关键一步：深度 = max(左子树深度, 右子树深度) + 1，空节点深度为 0。
- [108. Convert Sorted Array to Binary Search Tree](problems/0108_convert_sorted_array_to_binary_search_tree/notes.md)
  - 识别信号：输入是升序数组，要构造高度平衡的二叉搜索树；升序数组就是 BST 的中序遍历；"平衡"提示每次取中间元素当根
  - 关键一步：取区间中点作为根：左右两段大小最多差 1，整棵树自然高度平衡，且中序仍是原数组。
- [110. Balanced Binary Tree](problems/0110_balanced_binary_tree/notes.md)
  - 识别信号：判断每个节点左右子树高度差是否都不超过 1；既要子树的"是否平衡"，又要子树的"高度"，适合后序遍历一次返回两样信息
  - 关键一步：用 -1 表示"已不平衡"，非负数表示高度，一个返回值同时带回两种信息，每个节点只算一次。

## 哈希计数（6）

- [30. Substring with Concatenation of All Words](problems/0030_substring_with_concatenation_of_all_words/notes.md)
  - 识别信号：words 里所有单词等长，要找"所有单词各用一次、任意顺序拼成"的子串起点；任意顺序 → 比较单词的出现次数，而不是顺序；目标子串长度固定
  - 关键一步：按起点 mod w 把 s 拆成 w 条"单词流"，在每条流上做以单词为单位的滑动窗口，并用计数表维护窗口内每个单词的次数。
- [76. Minimum Window Substring](problems/0076_minimum_window_substring/notes.md)
  - 识别信号：求满足条件的"最短（或最长）连续子串 / 子数组"；条件可以在窗口左端或右端增减一个元素时增量更新（这里是字符计数）
  - 关键一步：维护 less = 还没凑够数量的字符种数：某字符的计数刚好达到需要的数量时 less 减 1，从刚好够变成不够时 less 加 1；less == 0 就说明窗口已经覆盖 t。
- [169. Majority Element](problems/0169_majority_element/notes.md)
  - 识别信号：多数元素的出现次数严格大于 n / 2，并且保证存在；进阶要求 O(n) 时间、O(1) 空间
  - 关键一步：多数元素超过一半，和其他元素两两抵消后剩下的一定是它；排序版本里，它的连续段一定覆盖下标 n // 2。
- [242. Valid Anagram](problems/0242_valid_anagram/notes.md)
  - 识别信号：判断两个字符串"字母相同、只是顺序不同"，即每个字符出现次数完全一致；顺序无关、只关心次数，就是在比较两份计数表
  - 关键一步：长度相等时，两份字符计数完全相同就是字母异位词；长度先判掉，就只需遍历一侧的键做比较。
- [274. H-Index](problems/0274_h_index/notes.md)
  - 识别信号：求最大的 h，使"至少有 h 个数 ≥ h"，答案随排序后的位置单调变化；h 不会超过数组长度 n，引用数大于 n 的都可以当作 n 处理（可以按次数分桶计数）
  - 关键一步：降序排序后，citations[i] ≥ i + 1 等价于"前 i + 1 篇的引用都至少是 i + 1"，所以 h 就是满足这个条件的最大 i + 1。
- [383. Ransom Note](problems/0383_ransom_note/notes.md)
  - 识别信号：magazine 里每个字母只能用一次，判断能否拼出 ransomNote，即比较两边每个字母的出现次数；只关心次数、不关心顺序
  - 关键一步：能拼出等价于：ransomNote 中每个字母的次数都不超过它在 magazine 中的次数。

## 滑动窗口（6）

- [3. Longest Substring Without Repeating Characters](problems/0003_longest_substring_without_repeating_characters/notes.md)
  - 识别信号：求满足条件（无重复字符）的"最长连续子串"；右端加入一个字符时，只需看这个字符是否已经在窗口里，可以 O(1) 判断
  - 关键一步：哈希表记录每个字符最后出现的下标；遇到重复字符时，只有它上次出现的位置还在窗口内（≥ l）才把左端移到该位置 + 1，左端只往右走。
- [30. Substring with Concatenation of All Words](problems/0030_substring_with_concatenation_of_all_words/notes.md)
  - 识别信号：words 里所有单词等长，要找"所有单词各用一次、任意顺序拼成"的子串起点；任意顺序 → 比较单词的出现次数，而不是顺序；目标子串长度固定
  - 关键一步：按起点 mod w 把 s 拆成 w 条"单词流"，在每条流上做以单词为单位的滑动窗口，并用计数表维护窗口内每个单词的次数。
- [76. Minimum Window Substring](problems/0076_minimum_window_substring/notes.md)
  - 识别信号：求满足条件的"最短（或最长）连续子串 / 子数组"；条件可以在窗口左端或右端增减一个元素时增量更新（这里是字符计数）
  - 关键一步：维护 less = 还没凑够数量的字符种数：某字符的计数刚好达到需要的数量时 less 减 1，从刚好够变成不够时 less 加 1；less == 0 就说明窗口已经覆盖 t。
- [209. Minimum Size Subarray Sum](problems/0209_minimum_size_subarray_sum/notes.md)
  - 识别信号：求和 ≥ target 的最短连续子数组；元素全是正数：右端扩张时和只增、左端收缩时和只减，满足滑动窗口需要的单调性
  - 关键一步：窗口和 ≥ target 时，固定左端继续扩右端只会更长，所以记录长度后直接把左端右移。
- [219. Contains Duplicate II](problems/0219_contains_duplicate_ii/notes.md)
  - 识别信号：判断是否存在两个相等的元素，且下标差 ≤ k；"距离不超过 k"：只关心每个值上一次出现的位置，或者维护长度为 k 的窗口
  - 关键一步：对同一个值，最近一次出现离当前位置最近；它都超过 k，更早的只会更远。
- [239. Sliding Window Maximum](problems/0239_sliding_window_maximum/notes.md)
  - 识别信号：固定长度 k 的滑动窗口，求每个窗口的最大值；n 可达 10^5、k 也可以很大，每个窗口重新求最大值会超时
  - 关键一步：一个元素如果比它后面进来的元素小，它在之后的任何窗口里都不可能是最大值，可以直接丢掉，所以队列保持单调递减。

## 矩阵模拟（6）

- [36. Valid Sudoku](problems/0036_valid_sudoku/notes.md)
  - 识别信号：只判断已填数字在每行、每列、每个 3×3 宫内不重复，不要求数独能解；判重 → 哈希表 / 集合；棋盘固定 9×9
  - 关键一步：用宫号公式 (i // 3)·3 + j // 3 把格子归到所在的 3×3 宫，这样行、列、宫的判重可以在同一遍扫描里完成。
- [48. Rotate Image](problems/0048_rotate_image/notes.md)
  - 识别信号：n × n 矩阵顺时针旋转 90 度；要求原地修改，不能另开一个矩阵
  - 关键一步：(i, j) 旋转后到 (j, n − 1 − i)；同一层的四个对应位置构成一个长度为 4 的环，用一个临时变量轮换即可原地完成。
- [54. Spiral Matrix](problems/0054_spiral_matrix/notes.md)
  - 识别信号：按顺时针螺旋顺序输出 m × n 矩阵的所有元素；纯过程模拟：右、下、左、上循环转向
  - 关键一步：每走完一条边就收缩对应的边界；走下一条边前检查 top ≤ bottom、left ≤ right，避免单行或单列被重复输出。
- [73. Set Matrix Zeroes](problems/0073_set_matrix_zeroes/notes.md)
  - 识别信号：原地修改矩阵，某个格子是 0 会影响它所在的整行和整列；边扫边改会让新写入的 0 继续"传染"，必须先记录、后修改
  - 关键一步：分两遍：先标记含 0 的行和列，再清零；O(1) 空间版本把这些标记存在第一行和第一列里。
- [289. Game of Life](problems/0289_game_of_life/notes.md)
  - 识别信号：所有格子要按"同一时刻的旧状态"同时更新，题目要求原地修改；每个格子的状态只有 0/1，可以用额外的数值同时编码"旧状态"和"新状态"
  - 关键一步：用 -1（原来活、现在死）和 2（原来死、现在活）两个中间值，让同一个格子同时保留旧状态和新状态，统计邻居时看的永远是旧状态。
- [733. Flood Fill](problems/0733_flood_fill/notes.md)
  - 识别信号：从一个格子出发，把上下左右连通、颜色相同的区域全部改色；"连通区域"在网格里就是 BFS / DFS 遍历
  - 关键一步：入队时立即改成新颜色，用"颜色是否还是原色"代替 visited 判断；新旧颜色相同时提前返回。

## 递归（6）

- [94. Binary Tree Inorder Traversal](problems/0094_binary_tree_inorder_traversal/notes.md)
  - 识别信号：要求按"左子树 → 根 → 右子树"的顺序输出节点值；进阶要求不用递归，提示要用显式栈模拟递归
  - 关键一步：中序就是"一路向左走到底，回来时记录当前节点，再去右子树"；递归和栈写法都只是在实现这个顺序。
- [100. Same Tree](problems/0100_same_tree/notes.md)
  - 识别信号：判断两棵树结构和节点值是否完全相同；结论可以拆成"根相同 且 左子树相同 且 右子树相同"
  - 关键一步：先处理"两个都空"和"只有一个空"这两种情况，剩下的就是值比较加左右递归。
- [101. Symmetric Tree](problems/0101_symmetric_tree/notes.md)
  - 识别信号：判断树是否是自身的镜像，也就是左子树和右子树互为镜像；进阶要求递归和迭代两种写法
  - 关键一步：比较的是成对的节点：左边的左孩子对右边的右孩子，左边的右孩子对右边的左孩子。
- [104. Maximum Depth of Binary Tree](problems/0104_maximum_depth_of_binary_tree/notes.md)
  - 识别信号：求根到最远叶子的节点数；整棵树的答案可以由左右子树的答案合成：max(左深度, 右深度) + 1
  - 关键一步：深度 = max(左子树深度, 右子树深度) + 1，空节点深度为 0。
- [108. Convert Sorted Array to Binary Search Tree](problems/0108_convert_sorted_array_to_binary_search_tree/notes.md)
  - 识别信号：输入是升序数组，要构造高度平衡的二叉搜索树；升序数组就是 BST 的中序遍历；"平衡"提示每次取中间元素当根
  - 关键一步：取区间中点作为根：左右两段大小最多差 1，整棵树自然高度平衡，且中序仍是原数组。
- [110. Balanced Binary Tree](problems/0110_balanced_binary_tree/notes.md)
  - 识别信号：判断每个节点左右子树高度差是否都不超过 1；既要子树的"是否平衡"，又要子树的"高度"，适合后序遍历一次返回两样信息
  - 关键一步：用 -1 表示"已不平衡"，非负数表示高度，一个返回值同时带回两种信息，每个节点只算一次。

## BFS（4）

- [45. Jump Game II](problems/0045_jump_game_ii/notes.md)
  - 识别信号：nums[i] 是从 i 最多能跳的距离，求到达最后一个位置的最少跳跃次数；保证能到达终点；求"最少步数" → 按步数分层（BFS），而每一层都是一段连续区间
  - 关键一步：第 s 步能到达的位置是连续的一段，扫到这一段的右边界 end 时必须再跳一次，新的右边界就是这一段里能跳到的最远位置 max_len。
- [101. Symmetric Tree](problems/0101_symmetric_tree/notes.md)
  - 识别信号：判断树是否是自身的镜像，也就是左子树和右子树互为镜像；进阶要求递归和迭代两种写法
  - 关键一步：比较的是成对的节点：左边的左孩子对右边的右孩子，左边的右孩子对右边的左孩子。
- [733. Flood Fill](problems/0733_flood_fill/notes.md)
  - 识别信号：从一个格子出发，把上下左右连通、颜色相同的区域全部改色；"连通区域"在网格里就是 BFS / DFS 遍历
  - 关键一步：入队时立即改成新颜色，用"颜色是否还是原色"代替 visited 判断；新旧颜色相同时提前返回。
- [2146. K Highest Ranked Items Within a Price Range](problems/2146_k_highest_ranked_items_within_a_price_range/notes.md)
  - 识别信号：网格里有墙（0）、空地（1）、商品（价格），每步上下左右走一格，排名第一关键字是"从起点出发的最短步数"；每步代价都是 1 的最短路，就是从起点做 BFS；排名规则是多关键字（距离、价格、行、列），收集后按元组排序
  - 关键一步：BFS 按层扩展天然按距离从小到大收集商品；某一层处理完时已收集够 k 个，就不必再往外走，剩下只需按 (距离, 价格, 行, 列) 排序。

## 区间（4）

- [56. Merge Intervals](problems/0056_merge_intervals/notes.md)
  - 识别信号：给一组区间，合并所有重叠的区间；输入无序；排序后，能合并的区间会相邻
  - 关键一步：按起点排序后，只需要和结果的最后一个区间比较。
- [57. Insert Interval](problems/0057_insert_interval/notes.md)
  - 识别信号：intervals 已按起点排序且互不重叠，插入一个新区间后仍要保持有序、不重叠；输入已有序 → 不需要再排序，一遍扫描即可
  - 关键一步：在有序且不重叠的输入里，和 newInterval 重叠的区间是连续的一段，把这一段和 newInterval 合并成一个区间即可。
- [228. Summary Ranges](problems/0228_summary_ranges/notes.md)
  - 识别信号：有序、无重复的整数数组，把连续的数合并成区间；输出每段连续区间的起点和终点
  - 关键一步：比较 nums[j] + 1 == nums[j + 1]，决定是延伸当前段还是新开一段。
- [452. Minimum Number of Arrows to Burst Balloons](problems/0452_minimum_number_of_arrows_to_burst_balloons/notes.md)
  - 识别信号：一组区间，用最少的"点"覆盖所有区间（一支箭就是一个 x 坐标）；端点相接也算重叠（x_start ≤ x ≤ x_end）
  - 关键一步：按起点排序后，当前组的交集右端是 min(各终点)；新气球起点 ≤ 这个右端就能共用一支箭，否则必须再射一支。

## 前后缀最大值（3）

- [42. Trapping Rain Water](problems/0042_trapping_rain_water/notes.md)
  - 识别信号：每个位置的答案 = min(左边最高, 右边最高) − 自身高度，即由"左右两侧的最大值"共同决定；原注释：这类需要计算左右最大高度的最小值的题，第一反应是从左到右取最大值，再从右到左取最大值，然后比较两者最小值，往往可以简化为维护单方向最大值，根据具体情况判断左右处理顺序
  - 关键一步：左右指针哪边当前高度更低就处理哪边：另一侧已经有一块不低于它的挡板，所以这个位置的水位只取决于它这一侧的最大值。
- [121. Best Time to Buy and Sell Stock](problems/0121_best_time_to_buy_and_sell_stock/notes.md)
  - 识别信号：只买卖一次，且必须先买后卖，求 prices[j] − prices[i]（i < j）的最大值；对每个卖出日，最优买入价就是它之前的最低价
  - 关键一步：从左往右扫，维护目前为止的最低价 min，每天的最大利润就是 price − min。
- [135. Candy](problems/0135_candy/notes.md)
  - 识别信号：每人至少 1 颗，评分比相邻高的要比相邻的多，求最少总数；约束同时来自左邻居和右邻居，可以拆成"只看左边"和"只看右边"两个方向分别满足
  - 关键一步：左右各扫一遍：第二遍只在"评分高于右邻且糖果不多于右邻"时改成右邻 + 1，这等价于取两个方向要求的最大值。

## 快慢指针（3）

- [19. Remove Nth Node From End of List](problems/0019_remove_nth_node_from_end_of_list/notes.md)
  - 识别信号：要删"倒数第 n 个"节点，而单链表只能从头往后走；进阶要求只遍历一次：让一个指针比另一个固定落后 n 步
  - 关键一步：后面的指针始终比前面的指针落后 n 步，停在待删节点的前驱；前面的指针走完时执行 前驱.next = 前驱.next.next。
- [141. Linked List Cycle](problems/0141_linked_list_cycle/notes.md)
  - 识别信号：判断链表是否有环；进阶要求 O(1) 额外空间，提示快慢指针
  - 关键一步：快指针每步比慢指针多走 1 步，进环后两者距离每步缩小 1，一定会相遇。
- [202. Happy Number](problems/0202_happy_number/notes.md)
  - 识别信号：反复做同一个变换，结果要么到达 1，要么无限循环；判断"是否进入循环"：记录见过的值，或者用快慢指针判环
  - 关键一步：平方和序列只能到 1 或进入循环，问题等价于判环：见过的数再次出现，就不是快乐数。

## 二分查找（2）

- [35. Search Insert Position](problems/0035_search_insert_position/notes.md)
  - 识别信号：有序、无重复的数组，找 target 的下标或应插入的位置；题目明确要求 O(log n)
  - 关键一步：插入位置就是"第一个 ≥ target 的下标"，二分到 left == right 时它就是答案。
- [69. Sqrt(x)](problems/0069_sqrt_x/notes.md)
  - 识别信号：求满足 k² ≤ x 的最大整数 k，而 k² 随 k 单调递增；不允许使用内置的开方或幂运算；x 最大到 2^31 − 1
  - 关键一步：k² ≤ x 对 k 单调，二分找最后一个满足的 k；牛顿迭代则用切线逼近 √x，整数部分稳定后即为答案。

## 前缀和（2）

- [134. Gas Station](problems/0134_gas_station/notes.md)
  - 识别信号：环形路线，从某个起点出发油量全程不能为负，求起点；题目保证有解时解唯一；总油量 ≥ 总消耗是有解的充要条件
  - 关键一步：从 start 出发到 i 时累计油量为负，则 start 到 i 之间都不能当起点，直接把起点跳到 i + 1。
- [238. Product of Array Except Self](problems/0238_product_of_array_except_self/notes.md)
  - 识别信号：每个位置的答案 = 左边所有数的乘积 × 右边所有数的乘积；不允许用除法、要求 O(n)；进阶要求 O(1) 额外空间（输出数组不计）
  - 关键一步：把"除自身以外的乘积"拆成左侧乘积 × 右侧乘积，两者都能一遍递推出来。

## 动态规划（2）

- [70. Climbing Stairs](problems/0070_climbing_stairs/notes.md)
  - 识别信号：求"有多少种走法"，每一步只有固定几种选择（1 阶或 2 阶）；到第 i 阶的方案数只依赖前一两阶的结果
  - 关键一步：最后一步不是跨 1 阶就是跨 2 阶，所以 f(n) = f(n − 1) + f(n − 2)，就是斐波那契数列。
- [121. Best Time to Buy and Sell Stock](problems/0121_best_time_to_buy_and_sell_stock/notes.md)
  - 识别信号：只买卖一次，且必须先买后卖，求 prices[j] − prices[i]（i < j）的最大值；对每个卖出日，最优买入价就是它之前的最低价
  - 关键一步：从左往右扫，维护目前为止的最低价 min，每天的最大利润就是 price − min。

## 堆（2）

- [239. Sliding Window Maximum](problems/0239_sliding_window_maximum/notes.md)
  - 识别信号：固定长度 k 的滑动窗口，求每个窗口的最大值；n 可达 10^5、k 也可以很大，每个窗口重新求最大值会超时
  - 关键一步：一个元素如果比它后面进来的元素小，它在之后的任何窗口里都不可能是最大值，可以直接丢掉，所以队列保持单调递减。
- [Booking: Minimum Sum](problems/booking_minimum_sum/notes.md)
  - 识别信号：题目（HackerRank，Booking 面试题）：给定整数数组 num 和整数 k，执行恰好 k 次操作，每次选一个元素 x 替换成 ceil(x / 2)，返回 k 次操作后数组之和的最小可能值；每次都要取"当前最大值"并把变小的值放回去，是典型的最大堆场景
  - 关键一步：每次操作都作用在当前最大值上，用最大堆维护"当前最大"。

## 设计（2）

- [155. Min Stack](problems/0155_min_stack/notes.md)
  - 识别信号：设计一个栈，push、pop、top、getMin 都要 O(1)；pop 之后最小值要"回退"到之前的状态，所以每个栈状态都要记住当时的最小值
  - 关键一步：push 时往 min_stack 压入 min(val, 当前最小值)，pop 时两个栈一起弹出，弹出后 min_stack 栈顶自动回到上一个状态的最小值。
- [380. Insert Delete GetRandom O(1)](problems/0380_insert_delete_getrandom_o_1/notes.md)
  - 识别信号：要求 insert、remove、getRandom 都是平均 O(1)；哈希表能 O(1) 增删查，但不能 O(1) 等概率随机取；数组能 O(1) 随机取，但不能 O(1) 删除中间元素，需要把两者结合
  - 关键一步：删除中间元素时，用数组末尾元素覆盖被删位置、更新末尾元素在哈希表里的下标，再 pop 末尾，避免数组整体移位。

## 位运算（1）

- [67. Add Binary](problems/0067_add_binary/notes.md)
  - 识别信号：两个二进制字符串相加，长度可达 10^4，不能指望转成固定宽度的整数（其他语言会溢出）；逐位相加加进位，和竖式加法一样
  - 关键一步：每一位的和 = a 位 ⊕ b 位 ⊕ 进位，新进位 = 三者中至少两个为 1；从右往左一遍扫完。

## 单调队列（1）

- [239. Sliding Window Maximum](problems/0239_sliding_window_maximum/notes.md)
  - 识别信号：固定长度 k 的滑动窗口，求每个窗口的最大值；n 可达 10^5、k 也可以很大，每个窗口重新求最大值会超时
  - 关键一步：一个元素如果比它后面进来的元素小，它在之后的任何窗口里都不可能是最大值，可以直接丢掉，所以队列保持单调递减。
