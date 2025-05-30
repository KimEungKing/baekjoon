import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main{

	private static class Node {
		String data;
		Node[] node;

		Node(String data) {
			this.data = data;
			node = new Node[27];
		}

		Node getChild(int index) {
			return node[index];
		}

		void setChilde(Node node, int index) {
			this.node[index] = node;
		}
	}

	private static class Trie {
		Node root;

		Trie() {
			this.root = new Node("");
		}

		void insert(String input) {
			Node tempNode = root;
			for (int i = 0; i <= input.length(); i++) {
				if (i != input.length()) {
					char c = input.charAt(i);
					int index = c - 'a';
					if (tempNode.getChild(index) == null) {
						Node n = new Node(String.valueOf(c));
						tempNode.setChilde(n, index);
						tempNode = n;
					} else {
						tempNode = tempNode.getChild(index);
					}
				} else {
					Node n = new Node("end");
					tempNode.setChilde(n, 26);
				}
			}
		}

		int clickNum(String input) {
			Node tempNode = root;
			int count = 1;
			for (int i = 0; i < input.length(); i++) {
				char c = input.charAt(i);
				int index = c - 'a';
				if (i != 0) {
					for (int j = 0; j < 27; j++) {
						if (j != index && tempNode.getChild(j) != null) {
							count++;
							break;
						} else if (tempNode.getChild(index) == null) {
							count++;
						}
					}
				}
				tempNode = tempNode.getChild(index);
			}
			return count;
		}
	}

	static int size;
	static ArrayList<String> list;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (true) {
//		for (int t = 0; t < 3; t++) {
			String input = br.readLine();
			if (input == null) {
				break;
			}
			list = new ArrayList<>();
			Trie trie = new Trie();
			int result = 0;
			size = Integer.parseInt(input);
			for (int i = 0; i < size; i++) {
				input = br.readLine();
				list.add(input);
				trie.insert(input);
			}

			for (String temp : list) {
				int count = trie.clickNum(temp);
				result += count;
			}

			double resultNum = (double) (result) / size;
			System.out.format("%.2f\n", resultNum);
		} 
	}
}
