public void addTrick(String trick) {
    LinkedList<String> temp = new LinkedList<String>(this.tricks);
    temp.add(trick);
    this.tricks = temp;
}
