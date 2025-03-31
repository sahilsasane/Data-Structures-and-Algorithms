import java.util.*;

public class main{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String inputString = scanner.nextLine();
        HashMap<Character,Integer> map = new HashMap<>();
        for(char c:inputString.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        HashSet<Character> done = new HashSet<>();
        StringBuilder output = new StringBuilder();
        for(char c:inputString.toCharArray()){
            if(!done.contains(c)){
                output.append(c);
                output.append(map.get(c));
                done.add(c);
            }

        }
        System.out.println(output.toString());
    }
}