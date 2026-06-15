/**
 * Minecraft面板侧边栏交互逻辑 - 简化版
 */
document.addEventListener('DOMContentLoaded', function() {
    // 获取DOM元素
    const navLinks = document.querySelectorAll('.nav-link');
    const submenuParents = document.querySelectorAll('.has-submenu');
    
    // 子菜单展开/收起功能
    submenuParents.forEach(parent => {
        const link = parent.querySelector('.nav-link');
        link.addEventListener('click', function(e) {
            // 如果是子菜单的链接，不阻止默认行为
            if (this.parentElement.classList.contains('has-submenu')) {
                e.preventDefault();
                
                // 切换当前子菜单的展开状态
                const isOpening = !parent.classList.contains('open');
                parent.classList.toggle('open');
                
                // 如果正在打开当前菜单，关闭其他已展开的菜单
                if (isOpening) {
                    submenuParents.forEach(otherParent => {
                        if (otherParent !== parent && otherParent.classList.contains('open')) {
                            otherParent.classList.remove('open');
                        }
                    });
                }
            }
        });
    });
    
    // 导航菜单点击事件
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // 如果是有子菜单的项，我们已经处理过了
            if (this.parentElement.classList.contains('has-submenu')) {
                return;
            }
            
            e.preventDefault();
            
            // 获取data-section属性
            const section = this.getAttribute('data-section');
            
            // 移除所有active类
            navLinks.forEach(l => l.classList.remove('active'));
            
            // 添加active类到当前点击的链接
            this.classList.add('active');
            
            // 更新内容区域
            updateContent(section);
        });
    });
    
    // 更新内容区域的函数
    function updateContent(section) {
        const contentTitle = document.getElementById('contentTitle');
        const contentSubtitle = document.getElementById('contentSubtitle');
        const contentSection = document.getElementById('contentSection');
        
        // 内容映射
        const contentMap = {
            'dashboard': {
                title: '服务器仪表盘',
                subtitle: '实时监控和管理您的Minecraft服务器',
                content: `
                    <div class="stats-grid">
                        <div class="stat-card">
                            <div class="stat-header">
                                <i class="fas fa-microchip"></i>
                                <h3>CPU使用率</h3>
                            </div>
                            <div class="stat-value">24%</div>
                            <div class="stat-progress">
                                <div class="progress-bar" style="width: 24%;"></div>
                            </div>
                        </div>
                        
                        <div class="stat-card">
                            <div class="stat-header">
                                <i class="fas fa-memory"></i>
                                <h3>内存使用</h3>
                            </div>
                            <div class="stat-value">2.3GB/8GB</div>
                            <div class="stat-progress">
                                <div class="progress-bar" style="width: 29%;"></div>
                            </div>
                        </div>
                        
                        <div class="stat-card">
                            <div class="stat-header">
                                <i class="fas fa-users"></i>
                                <h3>在线玩家</h3>
                            </div>
                            <div class="stat-value">12/50</div>
                            <div class="stat-progress">
                                <div class="progress-bar" style="width: 24%;"></div>
                            </div>
                        </div>
                        
                        <div class="stat-card">
                            <div class="stat-header">
                                <i class="fas fa-hdd"></i>
                                <h3>磁盘使用</h3>
                            </div>
                            <div class="stat-value">45GB/250GB</div>
                            <div class="stat-progress">
                                <div class="progress-bar" style="width: 18%;"></div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="recent-activities">
                        <h3><i class="fas fa-history"></i> 最近活动</h3>
                        <ul>
                            <li><span class="time">10:25</span> 玩家 "Steve" 加入了游戏</li>
                            <li><span class="time">10:18</span> 服务器自动备份完成</li>
                            <li><span class="time">09:45</span> 插件 "Essentials" 已更新</li>
                            <li><span class="time">09:30</span> 警告: 高延迟检测</li>
                            <li><span class="time">08:55</span> 玩家 "Alex" 离开了游戏</li>
                        </ul>
                    </div>
                `
            },
            'console': {
                title: '服务器控制台',
                subtitle: '实时查看服务器日志和执行命令',
                content: `
                    <div class="console-container">
                        <div class="console-output">
                            <div class="console-line">[10:25:12] [Server thread/INFO]: 服务器已启动，用时 4.567 秒</div>
                            <div class="console-line">[10:25:18] [Server thread/INFO]: Steve 加入了游戏</div>
                            <div class="console-line">[10:25:30] [Server thread/INFO]: Alex 加入了游戏</div>
                            <div class="console-line">[10:26:15] [Server thread/INFO]: Steve: 大家好！</div>
                            <div class="console-line">[10:26:40] [Server thread/INFO]: 执行了命令: /time set day</div>
                            <div class="console-line">[10:27:22] [Server thread/WARN]: 检测到实体数量过多，请考虑清理</div>
                        </div>
                        <div class="console-input">
                            <input type="text" placeholder="输入命令...">
                            <button><i class="fas fa-paper-plane"></i> 发送</button>
                        </div>
                    </div>
                `
            },
            'player-list': {
                title: '玩家管理',
                subtitle: '查看和管理在线玩家',
                content: `
                    <div class="player-list">
                        <div class="list-header">
                            <h3><i class="fas fa-users"></i> 在线玩家 (12)</h3>
                            <div class="list-actions">
                                <button class="btn btn-green"><i class="fas fa-plus"></i> 添加白名单</button>
                                <button class="btn btn-red"><i class="fas fa-ban"></i> 封禁玩家</button>
                            </div>
                        </div>
                        
                        <div class="player-grid">
                            <div class="player-card">
                                <div class="player-avatar">
                                    <i class="fas fa-user"></i>
                                </div>
                                <div class="player-info">
                                    <div class="player-name">Steve</div>
                                    <div class="player-details">
                                        <span><i class="fas fa-clock"></i> 在线: 1h 23m</span>
                                        <span><i class="fas fa-signal"></i> Ping: 45ms</span>
                                    </div>
                                </div>
                                <div class="player-actions">
                                    <button class="btn-icon" title="发送消息"><i class="fas fa-comment"></i></button>
                                    <button class="btn-icon" title="传送"><i class="fas fa-location-arrow"></i></button>
                                </div>
                            </div>
                            
                            <div class="player-card">
                                <div class="player-avatar">
                                    <i class="fas fa-user"></i>
                                </div>
                                <div class="player-info">
                                    <div class="player-name">Alex</div>
                                    <div class="player-details">
                                        <span><i class="fas fa-clock"></i> 在线: 45m</span>
                                        <span><i class="fas fa-signal"></i> Ping: 62ms</span>
                                    </div>
                                </div>
                                <div class="player-actions">
                                    <button class="btn-icon" title="发送消息"><i class="fas fa-comment"></i></button>
                                    <button class="btn-icon" title="传送"><i class="fas fa-location-arrow"></i></button>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            }
        };
        
        // 设置默认内容（如果类型不存在）
        const content = contentMap[section] || {
            title: section ? section.charAt(0).toUpperCase() + section.slice(1) : '仪表盘',
            subtitle: '功能内容',
            content: `
                <div class="welcome-message">
                    <div class="welcome-icon">
                        <i class="fas fa-tools"></i>
                    </div>
                    <h2>${section ? section.charAt(0).toUpperCase() + section.slice(1) : '功能'}</h2>
                    <p>此功能的内容将在这里显示</p>
                </div>
            `
        };
        
        // 更新标题和副标题
        contentTitle.textContent = content.title;
        contentSubtitle.textContent = content.subtitle;
        
        // 更新内容区域
        contentSection.innerHTML = content.content;
    }
    
    // 初始化 - 设置仪表盘为默认内容
    updateContent('dashboard');
});