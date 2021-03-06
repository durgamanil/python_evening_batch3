%sql
select t1.Week_Range,t1.cnpj_key,t1.ean_key,
case when (((t1.curr_price-t2.prev_price)/t2.prev_price)*100) <5 then '0-5%'
     when (((t1.curr_price-t2.prev_price)/t2.prev_price)*100) between 5 and 10 then '5-10%'
else '10-20%' end as Promotion_group from
(select concat(lag_week,'-',datekey) as Week_Range, cnpj_key, ean_key, (valor/volume_unidades) as curr_price from weeks_change) t1 inner join
(select concat(datekey,'-',lag_week) as Week_Range, cnpj_key, ean_key, (valor/volume_unidades) as prev_price from weeks_change where lag_week = datekey-7 and lag_week is not null) t2
on t1.cnpj_key = t2.cnpj_key and t1.ean_key = t2.ean_key
where t1.Week_Range is not null