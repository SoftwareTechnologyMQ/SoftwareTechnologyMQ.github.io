public class BalancingAct {
    public static void main(String[] args) {
        String s = "((()))";
        System.out.println("is " + s + " balanced: " + isBalanced(s));
        s = "(()())))";
        System.out.println("is " + s + " balanced: " + isBalanced(s));
        s = "(]{}[]";
        System.out.println("is " + s + " balanced: " + isBalanced(s));
        s = "(([{}]))";
        System.out.println("is " + s + " balanced: " + isBalanced(s));
    }

    public static boolean isBalanced(String brackets) {
        MyStack stk = new MyStack();
        String opening = "([{";
        String closing = ")]}";
        for (int i = 0; i < brackets.length(); i++) {
            char cur = brackets.charAt(i);
            if (opening.indexOf(cur) >= 0) { // if it's an opening bracket
                stk.push(cur + ""); // remember, ours is a stack that holds Strings
            } else if (closing.indexOf(cur) >= 0) { // closing bracket
                if (stk.isEmpty()) { // no matching opening bracket
                    return false;
                }
                String popped = stk.pop();
                if (opening.indexOf(popped) != closing.indexOf(cur)) { // not a match
                    return false;
                }
            } else { // some other character
                return false;
            }
        }
        return stk.isEmpty(); // only if stack is empty
    }
}
