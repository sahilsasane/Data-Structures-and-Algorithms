// package DS;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> cars = new ArrayList();
        cars.add(1);
        cars.add(2);
        cars.add(3);
        cars.add(4);
        cars.add(0, 99);
        System.out.println(cars);
        System.out.println(cars.get(0));
        cars.set(0, 54);
        cars.remove(0);
        System.out.println(cars.size());
        Collections.sort(cars);
        // Collections.sort(cars, Collections.reverseOrder());
        for (int i = 0; i < cars.size(); i++) {
            System.out.print(cars.get(i));
        }
        // cars.clear();
        LinkedList<String> llcars = new LinkedList();
        llcars.addFirst("Hello");
        llcars.addLast("bye");
        // llcars.removeFirst();
        // llcars.removeLast();
        // llcars.getFirst();
        // llcars.getLast();

        HashMap<String, String> capitalCities = new HashMap();
        capitalCities.put("England", "London");
        capitalCities.put("Germany", "Berlin");
        capitalCities.put("Norway", "Oslo");
        capitalCities.put("USA", "Washington DC");
        System.out.println(capitalCities);
        capitalCities.get("England");
        // .remove() .clear() .size()
        for (String i : capitalCities.values()) {
            System.out.println(i);
        }
        for (String i : capitalCities.keySet()) {
            System.out.println("key: " + i + " value: " + capitalCities.get(i));
        }

        HashSet<String> setcars = new HashSet(); // unique items
        // .contains(), .remove() .clear() .size()

        Iterator<Integer> it = cars.iterator();
        System.out.println(it.next());

        Pattern pattern = Pattern.compile("sahil", Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher("SahiL");
        boolean matchFound = matcher.find();
        if (matchFound) {
            System.out.println("Match found");
        } else {
            System.out.println("Match not found");
        }
    }
}
