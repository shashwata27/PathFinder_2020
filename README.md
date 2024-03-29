# **PathFinder_2020** : _Astar Algo_

A python game that uses Astar alogorithm to find the shortest path between source and destination,<br>
avoiding all the obstracles.

<img title="Pathfinder Logo" src="Images/pathfin.png" height=210 width=210>

**\*1StandAlone.exe** Folder can be seperatedly downloaded to play/test the game.*<br>
*No need to install python & encrypted data will be shown in console.\*

### Pathfinding Algorithm:

Astar algorithm is considered to be a _smart algorithm_ as it predicts the shortest path in each step, to find the acutal Shortest path.

- Works by using the sum _F(n)_.
- **_F(n)=G(n)+H(n)_**
  - Cost from the start node to the current node _G(n)_
  - Estimated cost from current node to goal _H(n)_.

### Encryption and Decryption Algorithm

**The key for Encryption and Decryption are synced and changes every 5 minutes.**

- User(client side) location and destination is encrypted before sending it to serverside path finding algorithm.
- Which decrypts it and finds the shortest path and sends back the path, which is again encrypted.
- When the client side GUI receives the encrypted path it decrypts it and shows it in the GUI.

  <!-- <p align="left">
  <img src="Images/en.PNG" width="512" height="246" title="Encryption Decryption">
  </p> -->

### Working:

- **Choose How big you want the Grid to be.**

  <p align="left">
  <img src="Images/1.PNG" width="350" title="Grid Size">
  </p>

- **Choose Source and Destination and also the Blockages.**

  <p align="left">
  <img src="Images/2.PNG" width="350" title="Source Destination Selection">
  </p>

- **Press Confrim then Show Path. The shortest Path gets Highlighted in yellow.**

  <p align="left">
  <img src="Images/3.PNG" width="350" title="Path Output">
  </p>

### Build:

- Used **pyInstaller** to create standalone release.

### Future:

- Deploy it in real world evironment, with real world data.
- Developing more ideas for encryption and decryption algorithms.
- Interating more pathfinding Algorithms for different cases.
- Making the UI mordern.
