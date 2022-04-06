# Reinforcement Learning 笔记

## 一、原理理解

``` markdown
贝尔曼方程，又叫动态规划方程，表示动态规划问题中相邻状态关系的方程。某些决策问题可以按照时间或空间分成多个阶段，每个阶段做出决策从而使整个过程取得效果最优的多阶段决策问题，可以用动态规划方法求解。**某一阶段最优决策的问题，通过贝尔曼方程转化为下一阶段最优决策的子问题，从而初始状态的最优决策可以由终状态的最优决策(一般易解)问题逐步迭代求解**。存在某种形式的贝尔曼方程，是动态规划方法能得到最优解的必要条件。绝大多数可以用最优控制理论解决的问题，都可以通过构造合适的贝尔曼方程来求解。
[内容来源: Bertsekas, D. P. (1976). Dynamic Programming and Stochastic Control. Academic Press, Inc.]
```



### （一）概述与符号

**“深度强化学习，就是在环境E下，由Agent根据状态S采取动作A，为了获得最大奖励R而不断训练生成策略P的过程。”**

强化学习也属于机器学习，那么我们研究的重点固然也是通过调参寻找一个适合的函数，这个函数就是策略P。而生成P的方法分为两种，基于策略的（Policy-based）和基于值的（Value-based），现在也有了两者的结合（Actor-Critic）。以下是通用符号：

- A：动作空间 Action
- S：状态空间 State
- R：奖励 Reward
- P：策略 Policy



- $\pi$ ：表示策略（policy）函数，参数常为环境返回的状态（state），输出为一个具体的动作（action），可知 $a=\pi(s)$ .
- $\pi_\theta$：使用参数$\theta$ 的策略$\pi$
- $r$ ：采取动作a后获得的即时奖励
- $G$ ：累积奖赏，$G_t$ 表示从时刻t开始到游戏结束的累积奖励（有时是$R_t$ ）

-  $\tau$ ：一轮游戏中把所有s，a和r串起来的时间序列（Trajectory） $$\tau=\{s_1,a_1,r_1,s_2,a_2,r_2,...,s_T,a_T，r_T\}$$  
- $\tau^n$ ：根据$p(\tau|\theta)$ 采样出来的过程$\tau$，$n$ 代表是采样第$n$次的得到的过程
- $p(\tau|\theta)$ ：Policy的参数为$\theta$ 时，采样采到$\tau$ 的概率
- $R_\theta$ ：参数为$\theta$ 时在一轮游戏中的累积奖赏，$R_\theta=\sum r_t$
- $R(\tau)$：游戏过程中所获取的奖励的总和，$R(\tau)=\sum_{t=1}^{T} r_t$

- $Q_\pi(s,a)$ ：状态-动作值函数（state-action value function）。表示在t时刻，状态s下，采取动作a，使用策略$\pi$ 预计获得的累积奖励的期望值

  <img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004223209654.png" alt="image-20201004223209654" style="zoom:70%;" />

- $V_\pi(s)$ ：状态值函数（state value function），表示在t时刻，状态s下使用策略$\pi$ 预计获得的累积奖励的期望值
  
  <img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004223245323.png" alt="image-20201004223245323" style="zoom:70%;" />

### （二）做决策的方法

事实上，这个Policy（Actor）可以不是神经网络，也可以其他的映射关系，例如一张表，每一个state对应一个action，但是这样数量庞大且死板，因此我们需要像NN这样有强大泛化能力的函数来作为Policy function。所以如果Policy是个NN，那么这个强化学习就是深度强化学习。

#### 0. On-Policy和Off-Policy

On-policy：Agent与环境互动，采样所用的Policy和目标Policy一致，采样后进行学习，学习后目标Policy更新，再用新的Policy去和环境互动，重新采样。

Off-policy：Agent通过别的Agent与环境互动所得来的数据更新自己的Policy，自己不参与互动，采样后的数据用很多次也没关系。

​	Off-policy之所以可以这么做，是通过**Importance Sampling**来实现的。

​	$E_{x\sim p}[f(x)]=E_{x\sim q}[f(x) \frac{p(x)}{q(x)}]$  

​	原先是从服从Policy1的p中采样，而现在是从服从Policy2的q中采样，要使被赋予Policy1的Agent能用q的样，我们就给q采出来的样乘	上一个权重$\frac{p(x)}{q(x)}$ ，使它接近Agent的Policy1。



#### 1. Policy-based和Value-based

- P-b（可连续可离散）通过优化**参数$\theta$** **直接**对策略进行优化

  1. Policy Gradient：梯度上升

- V-b（仅离散）通过**值函数V 或 Q 间接**对策略进行优化（遍历所有的状态和动作，找到能最大化值函数Q/V的策略）

  1. Dynamic Programming：动态规划

  2. Monte-Carlo Methods：蒙特卡洛算法

  3. Temporal-Difference Learning：时间差分学习

     包括Q-learning，DQN...

借用网上的一段形象描述：

```latex
V-B方法是对每一个状态下的行为进行打分，像是在训练一个裁判员（critic），根据这个裁判员对状态行为的评分，选择最高分，从而达到优化的结果。——P借助值函数知道自己玩得怎么样，再更新theta
P-B方法则不去管什么状态动作的评分，专心于优化自身。P-B方法就像是一个演员（actor），他只要把自己的参数学习好，自然就知道了什么状态下该选择什么动作。——P自己知道自己玩得怎么样，更新迭代theta 

P-B方法和V-B方法的区别在于前者训练的是策略本身（actor），而后者训练的是一种评判标准（critic）
```

#### 2. Policy-based

要训练一个Policy-based的方法，其实只需要三步。

1. 用一个神经网络作为策略，其参数为$\theta$ 

2. 设置一个Reward Function，告诉神经网络什么样的策略是好的，便有了优化的方向

3. 得到最佳策略

##### （1）Policy Gradient

​	对于这个神经网络，输入状态（state），输出对每一个动作（action）的选取概率，这就是神经网络做的工作，至于具体神经网络用什么模型，就得看实际情况。在一般的神经网络，我们都会用Cost Function去衡量输出的y_hat和真实值y的距离，再进行反向传播调参。但是强化学习中，我们并没有一个真实的y，所以在没有比较的情况下，我们通过给它奖励值Reward的方法，并期望这个奖励值能最大。

   “**用一个确定参数的神经网络去玩，行动轨迹会按一定概率分布。**”

   首先要明确**Episode**指什么，举个例子：当点击了开始游戏，经过N轮$\{s，a，r\}$后游戏结束，这叫一个Episode（而不是其中的一轮）。当然，对Agent这次玩游戏的表现，我们需要有个评估，而这次游戏的表现是由它一轮一轮面对s做出的a来决定的，所以我们对每一个a都返回一个reward（r），一个episode结束后，把所有r相加（T步累计奖赏），便得到：$R=\sum_{t=1}^{T}(r_t)$ ，如果我们让这个$R$ 最大化，那么无疑下次再遇到相同**Trajectory**时，Agent能给出最优策略。

   注意上面“遇到相同Trajectory”这句话，它警示了两点：

   1. 每把游戏的state，action都是随机的，所以Trajectory序列也是不同且随机的
   2. 因为序列不同，我们就算把上面这个R给最大化了，这个Agent也只能把上面所出现的Trajectory给出最优的action。那么结合1，我们的Agent就是在大海捞针

   所以什么是Trajectory呢？

$$\tau=\{s_1,a_1,s_2,a_2,...,s_T,a_T\}$$  

   它表示在一次Episode中把所有s和a串起来的集合。我们还用![p_{\theta}(\tau)](https://private.codecogs.com/gif.latex?p_%7B%5Ctheta%7D%28%5Ctau%29)表示在参数![\theta](https://private.codecogs.com/gif.latex?%5Ctheta)下Trajectory![\tau](https://private.codecogs.com/gif.latex?%5Ctau)发生的概率： $p_\theta(\tau)=p(s_1)\prod_{t=1}^{T}{p_\theta(a_t|s_t)p(s_{t+1}|s_t,a_t})$ 

   至此，我们更新对$R$ 的写法，写作$R(\tau)$ ，表示在$\tau$ 轨迹下那次episode的Reward，因为state和action 的随机性，可见它是个变量。那难道我们要穷举所有$R(\tau)$ 让它最大化保存下来，以便Agent遇到相同情况做出最佳策略吗？保存是不可能保存的，但可以**在给定$\theta$ 的情况下穷举所有可能的Trajectory，算出此时$R$ 的期望值$\overline{R}_\theta$，而为了使其最大化，就要去找到最佳的$\theta$ **。那么总的期望$\overline{R}_\theta$ 怎么来算呢？我们用每一种行动轨迹可能出现的概率乘上每一种行动轨迹的$R$ ，并全部求和来算。表示为：

   $$\overline{R}_\theta=\sum_{\tau}R(\tau)p_\theta(\tau)$$

   那么现在，我们只需要使$\overline{R}_\theta$ 最大化，求出对应的$\theta$ 即可得到最优策略$\pi_\theta$ 。在这里，我们使用**Policy gradient**的方法。推导如下：

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004222656923.png" alt="image-20201004222656923" style="zoom:63%;" />

这个对我们Policy function那个神经网络中的$\theta$ 求的梯度，可以这么来理解：

- $\overline{R}_\theta$ 的角标![\theta](https://private.codecogs.com/gif.latex?%5Ctheta)，是NN的参数，用来表征NN，而NN在这里是作为policy function来使用
- 第一个求和表示进行多次Episode，从而获得多个![\tau](https://private.codecogs.com/gif.latex?%5Ctau)
- 第二个求和表示对一个Episode的多个（s,a）对进行**采样**（采样![T_n](https://private.codecogs.com/gif.latex?T_n)次）
- 后面一坨![R\left(\tau^{n}\right) \nabla \log p_{\theta}\left(a_{t}^{n} | s_{t}^{n}\right)](https://private.codecogs.com/gif.latex?R%5Cleft%28%5Ctau%5E%7Bn%7D%5Cright%29%20%5Cnabla%20%5Clog%20p_%7B%5Ctheta%7D%5Cleft%28a_%7Bt%7D%5E%7Bn%7D%20%7C%20s_%7Bt%7D%5E%7Bn%7D%5Cright%29)，意思是如果这个![\tau](https://private.codecogs.com/gif.latex?%5Ctau)所得R比较大，那说明这个![\tau](https://private.codecogs.com/gif.latex?%5Ctau)表现得还不错，所以我们就会期望让这个![\tau](https://private.codecogs.com/gif.latex?%5Ctau)中的(s,a)出现的概率大一点，于是两者相乘，增大这个轨迹出现得概率；反之亦然。可见，$\theta$ 的优化会使得某轮游戏中的**所有行动a**在对应状态s下出现的概率提升或降低。

接下来，来对奖励函数做一些改进。

**1. Baseline**

由于（s，a）是通过采样的方式获得的，而奖励函数的值有时候会全正，那就会出现“一个极差的action得了正分，而一个未被采样的较好action没得分”的情况，基于此，我们给奖励函数添加一个**baseline**，使其有正有负：

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004225620624.png" alt="image-20201004225620624" style="zoom:50%;" />

**2. Attribute suitable credit** 

由于我们是根据一整轮游戏的结果来对所有$\tau$ 上的行为进行奖励，而非针对行为a本身，这显然不公平，但通过大数量的采样可以基本保证好的行为得到正的奖赏。但是，我们可以考虑直接对action进行奖赏或惩罚。我们不再整盘游戏的$R(\tau^n)$考虑 ，而是从行为所在的时间点开始累积奖励，又考虑到未来的奖励会受此时行为的影响较小，便添加一个折扣参数$\gamma$ 。具体如下：

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004225700803.png" alt="image-20201004225700803" style="zoom:50%;" />

其中$A^\theta(s_t,a_t)$ 被称为奖励函数：

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004231935085.png" alt="image-20201004231935085" style="zoom:55%;" />



#### 3. Value-based

##### （1）V-learning

​		在这个方法中，神经网络训练的是状态值函数$V_\pi(s)$

​		**1.1 蒙特卡罗方法（MC）**

​		求状态![[公式]](https://www.zhihu.com/equation?tex=s)处的值函数时,分为第一次访问蒙特卡罗方法和每次访问蒙特卡罗方法。更新状态值函数的公式为：

<img src="https://www.zhihu.com/equation?tex=%5C%5B+V%5Cleft%28S_t%5Cright%29%5Cgets+V%5Cleft%28S_t%5Cright%29%2B%5Calpha%5Cleft%28G_t-V%5Cleft%28S_t%5Cright%29%5Cright%29+%5C%5D" alt="[å¬å¼]" style="zoom:85%;" />

​		第一次访问蒙特卡罗方法是指，在计算状态s处值函数时，只利用每次Episode中第一次访问到状态s时的返回值，第一次访问蒙特卡罗方法的计算公式为：

<img src="https://www.zhihu.com/equation?tex=%5C%5B+%5Cupsilon%5Cleft%28s%5Cright%29%3D%5Cfrac%7BG_%7B11%7D%5Cleft%28s%5Cright%29%2BG_%7B21%7D%5Cleft%28s%5Cright%29%2B%5Ccdots%7D%7BN%5Cleft%28s%5Cright%29%7D+%5C%5D" alt="[公式]" style="zoom:85%;" />

​		每次访问蒙特卡罗方法是指，在计算状态![[公式]](https://www.zhihu.com/equation?tex=s)处的值函数时，利用所有访问到状态![[公式]](https://www.zhihu.com/equation?tex=s)时的回报返回值：

<img src="https://www.zhihu.com/equation?tex=%5C%5B+%5Cupsilon%5Cleft%28s%5Cright%29%3D%5Cfrac%7BG_%7B11%7D%5Cleft%28s%5Cright%29%2BG_%7B12%7D%5Cleft%28s%5Cright%29%2B%5Ccdots+%2BG_%7B21%7D%5Cleft%28s%5Cright%29%2B%5Ccdots%7D%7BN%5Cleft%28s%5Cright%29%7D+%5C%5D" alt="[公式]" style="zoom:85%;" />

​		**1.2 时序差分算法（TD）**

​		蒙特卡洛需要每次游戏结束才进行一次奖励值返还，而时序差分算法是由每次后一次状态的value和前一次状态value的差即时奖励r来调整状态值函数。更新状态值函数的公式为：

<img src="https://www.zhihu.com/equation?tex=%5C%5B+V%5Cleft%28S_t%5Cright%29%5Cgets+V%5Cleft%28S_t%5Cright%29%2B%5Calpha%5Cleft%28R_%7Bt%2B1%7D%2B%5Cgamma+V%5Cleft%28S_%7Bt%2B1%7D%5Cright%29-V%5Cleft%28S_t%5Cright%29%5Cright%29+%5C%5D" alt="[å¬å¼]" style="zoom:85%;" />

​		

##### （2）Q-learning

Q-learning实际上就是使用TD算法，通过每次的$r_t$ 对Q值函数进行优化，用到的公式即：

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004213057171.png" alt="image-20201004213057171" style="zoom:60%;" />

代码实现时，用到了三个技巧。

​		**2.1 Target network**

​		TD算法，训练一个模型当做Q函数。但是在实际过程中，不能让同一个神经网络同时输出两次Q值，所以，我们用Target Network（两个），固定网络B的参数不变，更新网络A的参数，更新次数达到一定值时，再将A的参数赋给B，再循环往复。diagram如下：

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004213954623.png" alt="image-20201004213954623" style="zoom:50%;" />

​		**2.2 Exploration**

​		回顾Policy Gradient：

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004214706620.png" alt="image-20201004214706620" style="zoom:65%;" />

​		在Policy Gradient中，我们是通过找到确定的$\theta$ 从而得到确定的策略$\pi$ ，从而得到action的概率分布。而在Q-learning中，action的		输出是确定的，因为优化Q函数就是通过最优a得到的：

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004215146894.png" alt="image-20201004215146894" style="zoom:65%;" />

​		那么会就产生了一个问题：如果在初始的采样过程中，某个action先获得了一定好的奖励，我们的神经网络Q函数就会一直选择这个		行为，而不会去探索（explore）选择其他行为了。对这个问题，可以通过以下两种方法来解决：

​		 **- Epsilon Greedy**

​		设置一个0到1间参数$\epsilon$ ，每次采取行动前都取个随机数值probility，如果数值小于$\epsilon$，那就随机行动；反之则采取最大Q值的那个行		为。一般来说，刚开始训练的时候，模型像张白纸一样，啥也不会，就应该把$\epsilon$取大一点，多去试试不同的action，训练多了之后再		去缩小。

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004220331809.png" alt="image-20201004220331809" style="zoom:62%;" />

​		 **- Boltzmann Exploration**

​		即softmax函数，把Q值函数代入softmax函数，输出在s情况下a出现的概率。

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004220707602.png" alt="image-20201004220707602" style="zoom:61%;" />

​		**2.3 Replay Buffer**

​		Replay Buffer就是一个用来存采样来的经验的存储空间，这里的经验就是一组一组的$s_t,a_t,r_t,s_{t+1}$ ，来源于不同的$\pi$ 与环境的交互。我们用Replay Buffer中的经验来训练Target Network（Off-Policy的体现）。

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004221909235.png" alt="image-20201004221909235" style="zoom:50%;" />

#### 4. Actor-Critic

其实就是用值函数表示了累计奖励，值函数通过v-b的方式拟合，最终策略通过p-b的方式拟合。

##### （1）A2C

在Policy-based的最后，我们得到：

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004230551492.png" alt="image-20201004230551492" style="zoom:50%;" />

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004231935085.png" alt="image-20201004231935085" style="zoom:55%;" />

其中表示累计奖励$R_t$ 的优势函数$A^\theta(s_t,a_t)$ 需要巨多的采样数据，才能训练得到较好的模型，于是就想到用对累计奖励的期望值来替代采样值。根据

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004223209654.png" alt="image-20201004223209654" style="zoom:70%;" />

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004223245323.png" alt="image-20201004223245323" style="zoom:70%;" />



我们得到

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004232040847.png" alt="image-20201004232040847" style="zoom:55%;" />

到这步之后，其实已经可以开始训练一个Q值函数的网络，一个V值函数的网络，但在经过一通公式操作，并结合一篇论文的发现，最终的A2C被优化成只用训练一个V值函数网络：

<img src="C:\Users\Symmetric_QIAN\AppData\Roaming\Typora\typora-user-images\image-20201004232359902.png" alt="image-20201004232359902" style="zoom:55%;" />



##### （2）A3C

多了一个A，Asynchronous，就是用很多个Work_Agent去玩，把取得的经验数据都给一个真正的Agent去学习。

# 二、代码实现



