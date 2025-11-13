
from algorithms import merge_sort, binary_search

def test_merge_sort_and_binary_search():
    seq = [5,3,8,1,9,2]
    sorted_seq = merge_sort(seq)
    assert sorted_seq == sorted(seq)
    found = binary_search(sorted_seq, 8, key=lambda x: x)
    assert found == 8

if __name__ == "__main__":
    test_merge_sort_and_binary_search()
    print("OK")
