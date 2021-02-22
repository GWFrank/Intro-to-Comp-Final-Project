# ItC HW7 Report

## A Reversi AI

### Requirements

Third-party Packages

` pip install neat-python`

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
- [x] Minimax with basic evaluate function (v1.0)
  - [x] Get Possible Moves
  - [x] Minimax
  - [x] Evaluate Function
  - [ ] Improve Performence
      - [x] Zobrist Hash
      - [ ] Use hash to lookup
- [x] NN evaluate function (v2.0)
    - [x] Remake the game without UI

### Current Branches
- `main` 是正式發行的版本分支
- `dev` 是主要的的工作分支，其他分支從這裡岔出
- `topic-init` 在做一些初始化的東東
- `topic-agent-basic` 在做agent要用的基本function
- `bugfix-typo` 用來修正打字錯誤
- `topic-2d-to-1d` 在把function間溝通用的index&list改成1d
- `topic-randomly-move` 讓agent有小機率會亂下一步
- `topic-zobrist-hash` 實做zobrist hash，用來hash盤面（還沒用到）
- `topic-agent-randomness` 處理不同盤面相同分數情況

### Resources
- [棋類AI(以五子棋為例)](https://reurl.cc/d5j9yV)
- [電腦黑白棋](https://reurl.cc/m9j7M1)
- [Reinforcement Learning and its Application to Othello](https://reurl.cc/d5jLQ6)
- [A Genetic Algorithm to Improve an Othello Program](https://reurl.cc/9XYxvn)

### Possible Implementations

- A : Mini-Max
  - 只有minimax，evaluate function直接寫死
  - evaluate function:
    - `posEval`: 直接一個每一格的價值表去加總
    - `posEvalEndgameVariation`: 在棋盤只剩下幾格時會用棋子數做計算，捨棄價值表

- B : Mini-Max + NN
  - 本質上就是minimax，用神經網路做evaluate function
- C : DL (沒做到)
  - 直接用不同策略的玩家對抗

### Agents
- `BetterRandomAgent`
  - Rule: 從所有可以下的地方隨機選一個
  - 節省測試時間用
- `BasicMinimaxAgent`
  - Rule: Minimax + 查表的evaluation，搜尋`d`層
  - Parameters: `d=5`, `eval_func=posEvalEndgameVariation`
- `LittleRandomAgent`
  - Rule: 每輪有機率`p`會是隨機下，`1-p`機率是走Minimax，搜尋`d`層
  - Parameters: `p=0.02`, `d=5`, `eval_func=posEvalEndgameVariation`
- `NEATAgent`
  - Rule: Minimax + 神經網路做的evaluation，搜尋`d`層
  - Parameters: `d=5`, `eval_func=NeuralNetwork`
  - Feed Forward Neural Network 用 NEAT 訓練
- Minor Tweaks
  - 前2步隨機走，增加遊戲的隨機性

### Test Data

#### `BasicMinimaxAgent` (先手) vs `RandomAgent`
| Depth        |     1 |     2 |     3 |     4 |     5 |     6 |
| ------------ | ----: | ----: | ----: | ----: | ----: | ----: |
| Games        |  5000 |  5000 |  5000 |  5000 |  5000 |  2000 |
| Wins         |  4404 |  4689 |  4841 |  4921 |  4954 |  1993 |
| Win%         |  .881 |  .938 |  .968 |  .984 |  .991 |  .997 |
| Sigma        | .0046 | .0034 | .0025 | .0018 | .0014 | .0013 |
| Win% - Sigma |  .876 |  .934 |  .966 |  .982 |  .989 |  .995 |
| Win% + Sigma |  .885 |  .941 |  .971 |  .986 |  .992 |  .998 |
#### `LittleRandomAgent` (先手) vs `RandomAgent`

| Depth        |     1 |     2 |     3 |     4 |     5 |     6 |
| ------------ | ----: | ----: | ----: | ----: | ----: | ----: |
| Games        |  5000 |  5000 |  5000 |  5000 |  5000 |  2000 |
| Wins         |  4446 |  4640 |  4818 |  4889 |  4951 |  1990 |
| Win%         |  .889 |  .928 |  .964 |  .978 |  .990 |  .995 |
| Sigma        | .0044 | .0037 | .0026 | .0021 | .0014 | .0016 |
| Win% - Sigma |  .885 |  .924 |  .961 |  .976 |  .989 |  .993 |
| Win% + Sigma |  .894 |  .932 |  .966 |  .980 |  .992 |  .997 |

#### `NEATAgent` (先手) vs `RandomAgent`
| Depth        |     1 |     2 |     3 |     4 |     5 |     6 |
| ------------ | ----: | ----: | ----: | ----: | ----: | ----: |
| Games        |  5000 |  5000 |  5000 |  5000 |  5000 |  2000 |
| Wins         |  4423 |  4659 |  4846 |  4926 |  4969 |  1987 |
| Win%         |  .885 |  .932 |  .969 |  .985 |  .994 |  .994 |
| Sigma        | .0045 | .0036 | .0024 | .0017 | .0011 | .0018 |
| Win% - Sigma |  .880 |  .928 |  .967 |  .983 |  .993 |  .992 |
| Win% + Sigma |  .889 |  .935 |  .972 |  .987 |  .995 |  .995 |

#### `NEATAgent` vs `BasicMinimaxAgent` (輪流先手)

| NEAT Wins | Basic Minimax Wins | Draw |
| --------: | -----------------: | ---: |
|      5002 |               4784 |  214 |