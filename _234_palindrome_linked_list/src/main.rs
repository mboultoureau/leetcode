fn main() {
    let test1 = vec![1, 2, 2, 1];
    let test2 = vec![1,2];

    let mut head = None;
    for i in test1.iter().rev() {
        let mut node = ListNode::new(*i);
        node.next = head;
        head = Some(Box::new(node));
    }

    assert!(Solution::is_palindrome(head));

    let mut head = None;
    for i in test2.iter().rev() {
        let mut node = ListNode::new(*i);
        node.next = head;
        head = Some(Box::new(node));
    }

    assert!(!Solution::is_palindrome(head));
}

pub struct Solution {}

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

impl Solution {
    pub fn is_palindrome(head: Option<Box<ListNode>>) -> bool {
        let mut numbers = Vec::new();
        let mut head = head;

        while head.is_some() {
            let node = head.unwrap();
            numbers.push(node.val);
            head = node.next;
        }

        let length = numbers.len();
        let mut i = 0;
        while i != length / 2 {
            if numbers[i] != numbers[length - i - 1] {
                return false;
            }

            i += 1;
        }

        true
    }
}