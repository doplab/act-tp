public void add_trick(String trick) {
        LinkedList temp = new LinkedList(this.tricks);
        temp.add(trick);
        this.tricks = temp;
    }