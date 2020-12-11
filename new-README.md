---
tags: Intro_to_Comp
---

<font face="Dejavu Sans"/>

# ItC HW7 Report

## A Reversi AI

### Team members

- Team leader
  - Name: Huai-Yuan Kuo
  - Student ID: B09902004
  - Github: [GWFrank](https://github.com/GWFrank)
- Member
  - Name: Jun-Wei Liu
  - Student ID: B09902009
  - Github: [Letuvertia](https://github.com/Letuvertia)
- Member
  - Name: Ko-Bang Chen
  - Student ID: B09902011
  - Github: [ChenKB91](https://github.com/ChenKB91)

### Progress
- [x] Copy & paste RandomAgent (v0.0)
- [ ] Minimax with basic evaluate function (v1.0)
  - [x] Get Possible Moves
  - [x] Minimax
  - [x] Evaluate Function
  - [ ] Improve Performence
      - [x] Zobrist Hash
      - [ ] Use hash to lookup
- [ ] NN evaluate function, trained with GA
    - [x] Remake the game without UI
    - [ ] Research popular packages like tensorflow, pytorch, keras

### Current Branches
- `main` 是正式發行的版本分支
- `dev` 是主要的的工作分支，其他分支從這裡岔出
- `topic-init` 在做一些初始化的東東
- `topic-agent-basic` 在做agent要用的基本function
- `bugfix-typo` 用來修正打字錯誤
- `topic-2d-to-1d` 在把function間溝通用的index&list改成1d
- `topic-randomly-move` 讓agent有小機率會亂下一步（尚在測試中）
- `topic-zobrist-hash` 實做zobrist hash，用來hash盤面（還沒用到）
- `topic-agent-randomness` 處理不同盤面相同分數情況

### Resources
- [棋類AI(以五子棋為例)](https://reurl.cc/d5j9yV)
- [電腦黑白棋](https://reurl.cc/m9j7M1)
- [Reinforcement Learning and its Application to Othello](https://reurl.cc/d5jLQ6)
- [A Genetic Algorithm to Improve an Othello Program](https://reurl.cc/9XYxvn)

### 實作方法
- Case A : Mini-Max + NN
  - 本質上就是minimax，用神經網路做evaluate function
- Case B : DL
  - 直接用不同策略的玩家對抗
- Case C : Mini-Max
  - 只有minimax，evaluate function直接寫死

### Agents
- `BetterRandomAgent`
  - Rule: 從所有可以下的地方隨機選一個
  - 節省測試時間用
- `BasicMinimaxAgent`
  - Rule: Minimax with 查表的evaluation，搜尋$d$層
  - Parameters: $d=5$
- `LittleRandomAgent`
  - Rule: 每輪有機率$p$會是隨機下，$1-p$機率是走Minimax，搜尋$d$層
  - Parameters: $p=1/32$, $d=5$

### Some Datas

#### BasicMinimaxAgent (goes first) vs BetterRandomAgent
Depth        |     1 |     2 |     3 |     4 |     5 |     6 |
------------ | -----:| -----:| -----:| -----:| -----:| -----:|
Games        |  5000 |  5000 |  5000 |  5000 |  5000 |  2000 |
Win%         |  .878 |  .880 |  .883 |  .902 |  .911 |  .858 |
Sigma        | .0046 | .0046 | .0046 | .0042 | .0040 | .0078 |
Win% - Sigma |  .873 |  .875 |  .878 |  .898 |  .907 |  .850 |
Win% + Sigma |  .883 |  .885 |  .887 |  .906 |  .915 |  .866 |
- 做5層搜尋似乎有最好的表現，且運行時間夠快(sub-5, Ryzen 3600 @ Linux)
- 預留時間給後面要加的feature

#### LittleRandomAgent vs BasicMinimaxAgent

