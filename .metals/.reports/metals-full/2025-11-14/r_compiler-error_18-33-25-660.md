file://<WORKSPACE>/2025/week10/solutions/Question5.java
### java.util.NoSuchElementException: next on empty iterator

occurred in the presentation compiler.

presentation compiler configuration:


action parameters:
uri: file://<WORKSPACE>/2025/week10/solutions/Question5.java
text:
```scala
public class Question5 {
    // Fusionne 2 sous-listes de arr[].
    // Première sous-liste est arr[l..m]
    // Deuxième sous-liste est arr[m+1..r]
    public static void merge(int arr[], int l, int m, int r) {
        // Trouver la taille des deux sous-listes à fusionner
        int n1 = m - l + 1;
        int n2 = r - m;

        /* Créer des listes temporaires */
        int L[] = new int[n1];
        int R[] = new int[n2];

        /* Copier les données dans les sous-listes temporaires */
        for (int i = 0; i < n1; ++i) {
            L[i] = arr[l + i];
        }
        for (int j = 0; j < n2; ++j) {
            R[j] = arr[m + 1 + j];
        }

        /* Fusionner les sous-listes temporaires */
        // Indexes initiaux de la première et seconde sous-liste
        int i = 0, j = 0;

        // Index initial de la sous-liste fusionnée
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        /* Copier les élements restants de L[] */
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        /* Copier les élements restants de R[] */
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    // Fonction principale qui trie arr[l..r] en utilisant
    // merge()
    public static void tri_fusion(int arr[], int l, int r) {
        if (l < r) {
            // Trouver le milieu de la liste
            int m = (l + r) / 2;

            // Trier les première et la deuxième parties de la liste
            tri_fusion(arr, l, m);
            tri_fusion(arr, m + 1, r);

            // Fusionner les deux parties
            merge(arr, l, m, r);
        }
    }

    public static void affiche_liste(int l[]) {
        int n = l.length;
        for (int i = 0; i < n; ++i)
            System.out.println(l[i] + " ");
    }

    public static void main(String[] args) {
        int[] l = { 38, 27, 43, 3, 9, 82, 10 };
        tri_fusion(l, 0, l.length - 1);
        affiche_liste(l);
    }
}

```



#### Error stacktrace:

```
scala.collection.Iterator$$anon$19.next(Iterator.scala:973)
	scala.collection.Iterator$$anon$19.next(Iterator.scala:971)
	scala.collection.mutable.MutationTracker$CheckedIterator.next(MutationTracker.scala:76)
	scala.collection.IterableOps.head(Iterable.scala:222)
	scala.collection.IterableOps.head$(Iterable.scala:222)
	scala.collection.AbstractIterable.head(Iterable.scala:935)
	dotty.tools.dotc.interactive.InteractiveDriver.run(InteractiveDriver.scala:164)
	dotty.tools.pc.MetalsDriver.run(MetalsDriver.scala:45)
	dotty.tools.pc.WithCompilationUnit.<init>(WithCompilationUnit.scala:31)
	dotty.tools.pc.SimpleCollector.<init>(PcCollector.scala:345)
	dotty.tools.pc.PcSemanticTokensProvider$Collector$.<init>(PcSemanticTokensProvider.scala:63)
	dotty.tools.pc.PcSemanticTokensProvider.Collector$lzyINIT1(PcSemanticTokensProvider.scala:63)
	dotty.tools.pc.PcSemanticTokensProvider.Collector(PcSemanticTokensProvider.scala:63)
	dotty.tools.pc.PcSemanticTokensProvider.provide(PcSemanticTokensProvider.scala:88)
	dotty.tools.pc.ScalaPresentationCompiler.semanticTokens$$anonfun$1(ScalaPresentationCompiler.scala:109)
```
#### Short summary: 

java.util.NoSuchElementException: next on empty iterator