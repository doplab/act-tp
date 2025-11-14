error id: file://<WORKSPACE>/2025/week10/solutions/Question3.java
file://<WORKSPACE>/2025/week10/solutions/Question3.java
### com.thoughtworks.qdox.parser.ParseException: syntax error @[28,2]

error in qdox parser
file content:
```java
offset: 734
uri: file://<WORKSPACE>/2025/week10/solutions/Question3.java
text:
```scala
public class Question3 {
    public static void tri_bulle(int[] l) {
        int n = l.length;
        for (int i = 0; i < n - 1; i++){
            for (int j = 0; j < n-i-1; j++) {
                if (l[j] > l[j+1]) { 
                    // échange l[j+1] et l[i] 
                    int temp = l[j]; 
                    l[j] = l[j+1]; 
                    l[j+1] = temp; 
                } 
        }
    }

    public static void printArray(int l[]) {
        int n = l.length;
        for (int i = 0; i < n; ++i)
            System.out.print(l[i] + " ");

        System.out.println();
    }

    public static void main(String[] args) {
        int[] l = { 1, 2, 4, 3, 1 };
        tri_bulle(l);
        printArray(l);
    }
}@@
```

```



#### Error stacktrace:

```
com.thoughtworks.qdox.parser.impl.Parser.yyerror(Parser.java:2025)
	com.thoughtworks.qdox.parser.impl.Parser.yyparse(Parser.java:2147)
	com.thoughtworks.qdox.parser.impl.Parser.parse(Parser.java:2006)
	com.thoughtworks.qdox.library.SourceLibrary.parse(SourceLibrary.java:232)
	com.thoughtworks.qdox.library.SourceLibrary.parse(SourceLibrary.java:190)
	com.thoughtworks.qdox.library.SourceLibrary.addSource(SourceLibrary.java:94)
	com.thoughtworks.qdox.library.SourceLibrary.addSource(SourceLibrary.java:89)
	com.thoughtworks.qdox.library.SortedClassLibraryBuilder.addSource(SortedClassLibraryBuilder.java:162)
	com.thoughtworks.qdox.JavaProjectBuilder.addSource(JavaProjectBuilder.java:174)
	scala.meta.internal.mtags.JavaMtags.indexRoot(JavaMtags.scala:48)
	scala.meta.internal.mtags.MtagsIndexer.index(MtagsIndexer.scala:21)
	scala.meta.internal.mtags.MtagsIndexer.index$(MtagsIndexer.scala:20)
	scala.meta.internal.mtags.JavaMtags.index(JavaMtags.scala:38)
	scala.meta.internal.mtags.Mtags$.allToplevels(Mtags.scala:150)
	scala.meta.internal.metals.DefinitionProvider.fromMtags(DefinitionProvider.scala:355)
	scala.meta.internal.metals.DefinitionProvider.$anonfun$positionOccurrence$4(DefinitionProvider.scala:274)
	scala.Option.orElse(Option.scala:477)
	scala.meta.internal.metals.DefinitionProvider.$anonfun$positionOccurrence$1(DefinitionProvider.scala:274)
	scala.Option.flatMap(Option.scala:283)
	scala.meta.internal.metals.DefinitionProvider.positionOccurrence(DefinitionProvider.scala:266)
	scala.meta.internal.metals.JavaDocumentHighlightProvider.$anonfun$documentHighlight$1(JavaDocumentHighlightProvider.scala:26)
	scala.collection.immutable.List.map(List.scala:247)
	scala.meta.internal.metals.JavaDocumentHighlightProvider.documentHighlight(JavaDocumentHighlightProvider.scala:22)
	scala.meta.internal.metals.MetalsLspService.$anonfun$documentHighlights$1(MetalsLspService.scala:1008)
	scala.meta.internal.metals.CancelTokens$.$anonfun$apply$2(CancelTokens.scala:26)
	scala.concurrent.Future$.$anonfun$apply$1(Future.scala:687)
	scala.concurrent.impl.Promise$Transformation.run(Promise.scala:467)
	java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1136)
	java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:635)
	java.base/java.lang.Thread.run(Thread.java:840)
```
#### Short summary: 

QDox parse error in file://<WORKSPACE>/2025/week10/solutions/Question3.java