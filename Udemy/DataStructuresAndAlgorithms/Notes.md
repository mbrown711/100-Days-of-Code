## What is good code?

1. Readable
2. Scalable - this is where Big O comes in

```javascript
const nemo = ['nemo'];
const everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank'];

const large = new Array(10000).fill('nemo');

function findNemo(array) {
    let t0 = performance.now();
    for (let i = 0; i < array.length; i++) {
        if (array[i] == 'nemo') {
            console.log('Found Nemo!');
        }
    }
    let t1 = performance.now();
    console.log('Call to find nemo took ' + (t1 - t0) + ' milliseconds');
}

findNemo(large);
```

```java
import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        String[] nemo = {"nemo"};

        String[] everyone = {"dory", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt", "darla", "hank"};

        String[] bigArray = new String[100];

        Arrays.fill(bigArray, "nemo");

        for (int i = 0; i < bigArray.length; i++) {
            System.out.println(bigArray[i]);
        }
    }
}
```