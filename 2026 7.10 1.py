import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: f'{x:.2f}')

orders = pd.DataFrame({
    'order_id': ['1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010',
                 '1011', '1012', '1013', '1014', '1015', '1016', '1017', '1018', '1019'],
    'region': ['华东', '华北', '华南', '华东', '西南', '华北', '华南', '华东', '西南', '华北',
               '华东', '华南', '西南', '华东', '华北', '华南', '华东', '西南', '华东'],
    'product': ['机械键盘', '无线鼠标', '显示器', '扩展坞', '机械键盘', '显示器', '无线鼠标', '显示器',
                '扩展坞', '机械键盘', '显示器', '无线鼠标', '显示器', '扩展坞', '机械键盘', '显示器',
                '无线鼠标', '显示器', '扩展坞'],
    'category': ['外设', '外设', '显示设备', '配件', '外设', '显示设备', '外设', '显示设备', '配件',
                 '外设', '外设', '配件', '显示设备', '外设', '外设', '配件', '显示设备', '外设', '配件'],
    'quantity': [2,3,1,4,5,2,6,1,3,2,8,2,1,3,5,2,4,6,1],  # ✅ 补上最后一个1，共19个
    'unit_price': [289,129,299,399,289,129,399,289,129,399,289,399,1299,289,399,1299,129,289,129],
    'member_level': ['金卡', '普通', '银卡', '金卡', '银卡', '普通', '金卡', '银卡', '普通', '金卡',
                     '银卡', '金卡', '普通', '银卡', '金卡', '普通', '银卡', '金卡', '普通'],
    'coupon_rate': [0.05,0.00,0.00,0.08,0.10,0.05,0.00,0.12,0.05,0.00,0.00,0.08,0.10,0.05,0.00,0.12,0.05,0.00,0.08],
    'salesperson': ['小林', '小周', '小陈', '小林', '小赵', '小周', '小陈', '小林', '小赵', '小周',
                    '小林', '小陈', '小赵', '小林', '小周', '小陈', '小林', '小赵', '小周']
})

# 任务1
print("行数、列数、列名：", orders.shape, orders.columns.tolist())
print("region单列类型：", orders['region'].dtype)
print("order_id/product/quantity三列类型：", orders[['order_id','product','quantity']].dtypes)
print("第4-8行、前4列：\n", orders.iloc[3:8, :4])
print("华东订单的order_id/product/member_level：\n", orders.loc[orders['region']=='华东', ['order_id','product','member_level']])
print("loc更推荐是因为它支持标签索引，代码更易读且不易因行号变动出错。")

# 任务2
analysis = orders.copy()
analysis['gross_amount'] = analysis['quantity'] * analysis['unit_price']
analysis['member_discount'] = np.where(analysis['member_level']=='金卡', 0.1,
                                       np.where(analysis['member_level']=='银卡', 0.05, 0))
analysis['payable_amount'] = analysis['gross_amount'] * (1 - analysis['member_discount']) * (1 - analysis['coupon_rate'])
analysis['shipping_fee'] = np.where(analysis['payable_amount'] >= 1000, 0, 20)
analysis['final_amount'] = analysis['payable_amount'] + analysis['shipping_fee']
print("analysis前8行：\n", analysis.head(8))

# 任务3
cond1 = analysis['region'].isin(['华东','华南'])
cond2 = analysis['final_amount'] >= 700
cond3 = (analysis['quantity'] >= 2) | (analysis['member_level'] == '金卡')
mask = (cond1 & cond2) & cond3
focus_orders = analysis.loc[mask, ['order_id','region','product','quantity','member_level','final_amount']]
focus_orders = focus_orders.sort_values('final_amount', ascending=False)
print("重点跟进订单：\n", focus_orders)
print("&两侧加括号是为了保证运算顺序，先算每个条件内部，再组合，避免逻辑错误。")

# 任务4
def add_order_level(df):
    return df.assign(order_level=np.where(df['final_amount'] >= 2000, '战略订单',
                                          np.where(df['final_amount'] >= 1000, '重点订单', '普通订单')))
leveled_orders = analysis.pipe(add_order_level)
print("各等级订单数：\n", leveled_orders['order_level'].value_counts())

# 任务5
region_report = (analysis
                 .pipe(add_order_level)
                 .query('final_amount >= 500')
                 .groupby(['region','order_level'])
                 .agg(order_count=('order_id','count'),
                      quantity_sum=('quantity','sum'),
                      revenue_sum=('final_amount','sum'),
                      revenue_mean=('final_amount','mean'))
                 .sort_values('revenue_sum', ascending=False))
print("地区经营汇总：\n", region_report)

# 任务6
top_sales = analysis.groupby('salesperson')['final_amount'].sum().idxmax()
top_region = analysis[analysis['salesperson']==top_sales].groupby('region')['final_amount'].sum().idxmax()
top_amount = analysis[(analysis['salesperson']==top_sales) & (analysis['region']==top_region)]['final_amount'].sum()
total_amount = analysis[analysis['salesperson']==top_sales]['final_amount'].sum()
ratio = top_amount / total_amount
print(f"销售人员：{top_sales}，核心地区：{top_region}，总成交金额：{total_amount:.2f}，核心地区金额：{top_amount:.2f}，地区贡献率：{ratio:.2%}")
print("业务结论：该销售人员在核心地区贡献了超过半数的成交金额，应持续深耕该地区。")