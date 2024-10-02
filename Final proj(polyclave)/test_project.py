from project import find_target_key,perform_filter,remove_feature
import pytest

test_dict = [
    {'name':'A','feature1': 'Yes', 'feature2': 'No'},
    {'name':'B','feature1': 'No', 'feature2': 'Yes'},
    {'name':'C','feature1': 'No', 'feature2': 'Yes'},
    {'name':'D','feature1': 'Yes', 'feature2': 'Yes'}
    ]

def test_find_target_key():
    assert find_target_key(test_dict) == 'feature1'


def test_perform_filter():
    filtered_list = perform_filter(test_dict, 'feature1', 'Yes')
    assert len(filtered_list) == 2
    assert filtered_list[0] == {'name':'A','feature1': 'Yes', 'feature2': 'No'}
    assert filtered_list[1] == {'name':'D','feature1': 'Yes', 'feature2': 'Yes'}

def test_remove_feature():
    expected1=[
    {'name':'A', 'feature2': 'No'},
    {'name':'B', 'feature2': 'Yes'},
    {'name':'C', 'feature2': 'Yes'},
    {'name':'D', 'feature2': 'Yes'}
    ]
    assert remove_feature(test_dict, 'feature1')== expected1
    expected2=[
    {'name':'A', 'feature1': 'Yes'},
    {'name':'B', 'feature1': 'No'},
    {'name':'C', 'feature1': 'No'},
    {'name':'D', 'feature1': 'Yes'}
    ]
    assert remove_feature(test_dict, 'feature2')== expected2
