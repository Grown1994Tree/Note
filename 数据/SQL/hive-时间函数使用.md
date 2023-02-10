### 一、时间戳转换

```sql
-- 根据指定格式的日期字符串转换成时间戳
unix_timestamp("20220101","yyyyMMdd")
unix_timestamp("2022-01-01","yyyy-MM-dd")

-- 把时间戳转换成日期对象
from_timestamp(1640966400)
```

### 二、特殊日期获取

```SQL
-- 获得每周的周一
date_sub(next_date(date,"MO"),7)

-- 获得每周的周日
date_sub(next_date(date,"MO"),1)

-- 获取每月月末
last_day(date)

-- 获取每月月初
trunc(date,"MM")
```

### 三、生成时间列表

```sql
with dates as (
    select
        dateadd(base_date,pos)  as `base_date`
    from (
        select datediff(end_date,begin_date) as `date_count`,begin_date as `base_date`
    ) v
    LATEVAL VIEW posexplode(split(repeat('1,',date_count),',')) view1 as pos,val
)
```

### 四、计算月_周数

```sql
-- 按照月数分组，再按照每周的周一进行紧凑排序
select 
    dense_rank() over(partition by substr(format_date(base_date,"yyyyMMdd"),1,6) order by date_sub(next_date(base_date,"MO"),7))
from dates
```
