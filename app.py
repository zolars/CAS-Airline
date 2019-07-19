import json
import random

from flask import Flask, render_template
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

from pyecharts import options as opts
from pyecharts.charts import Geo, Grid
from pyecharts.globals import ChartType, SymbolType, ThemeType


app = Flask(__name__, static_folder="templates")


def get_airports():
    f_data = open("data.json", "r", encoding="utf-8")
    data = json.load(f_data)

    airports_list = []
    for i in data:
        for j in i["airlines"]:
            airports_list.append(j["from"])
            airports_list.append(j["to"])

    return airports_list, data


def airports_map(airports_list, data) -> Geo:
    colors = ['#a6c84c', '#ffa022', '#46bee9']
    airports_value = [list("") for i in airports_list]

    c = (
        Geo(init_opts=opts.InitOpts(
            chart_id="airline",
            theme=ThemeType.ROMANTIC,
            width="100%",
            height="760px",
            page_title="Airline Map"
        ))
        .add_schema(
            maptype="world",
            is_roam=False,
            itemstyle_opts=opts.ItemStyleOpts(
                color="#323c48", border_color="#404a59")
        )
        .add_coordinate_json("airports.json")
        .add(None, [list(z) for z in zip(airports_list, airports_value)], type_=ChartType.EFFECT_SCATTER,
             effect_opts=opts.EffectOpts(is_show=False, brush_type="stroke"))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Airline Map"),
            legend_opts=opts.LegendOpts(
                type_="scroll",
                selected_mode="single",
                orient="vertical",
                pos_left="3%",
                pos_top="100px"
            ),
        )
    )

    # 添加全体航线 会导致卡顿 暂时弃用
    # airlines_all = []
    # for i in data:
    #     for j in i["airlines"]:
    #         airlines_all.append((j["from"], j["to"]))

    # for i in airlines_all:
    #     color = random.choice(colors)
    #     c.add(
    #         "All",
    #         [i],
    #         type_=ChartType.LINES,
    #         is_large=True,
    #         effect_opts=opts.EffectOpts(
    #             color=color,
    #             is_show=True,
    #             trail_length=0,
    #             symbol='path://M1705.06,1318.313v-89.254l-319.9-221.799l0.073-208.063c0.521-84.662-26.629-121.796-63.961-121.491c-37.332-0.305-64.482,36.829-63.961,121.491l0.073,208.063l-319.9,221.799v89.254l330.343-157.288l12.238,241.308l-134.449,92.931l0.531,42.034l175.125-42.917l175.125,42.917l0.531-42.034l-134.449-92.931l12.238-241.308L1705.06,1318.313z',
    #             symbol_size=22,
    #             period=random.randint(4, 10)

    #         ),
    #         linestyle_opts=opts.LineStyleOpts(
    #             color=color,
    #             opacity=0.5,
    #             type_="solid",
    #             curve=0.2),
    #     )

    # 添加单体航线
    for i in data:
        airlines = []
        for j in i["airlines"]:
            airlines.append((j["from"], j["to"]))
        for j in airlines:
            color = random.choice(colors)
            c.add(
                i["name"],
                [j],
                type_=ChartType.LINES,
                effect_opts=opts.EffectOpts(
                    color=color,
                    is_show=True,
                    trail_length=0,
                    symbol='path://M1705.06,1318.313v-89.254l-319.9-221.799l0.073-208.063c0.521-84.662-26.629-121.796-63.961-121.491c-37.332-0.305-64.482,36.829-63.961,121.491l0.073,208.063l-319.9,221.799v89.254l330.343-157.288l12.238,241.308l-134.449,92.931l0.531,42.034l175.125-42.917l175.125,42.917l0.531-42.034l-134.449-92.931l12.238-241.308L1705.06,1318.313z',
                    symbol_size=22,
                    period=random.randint(4, 10)

                ),
                linestyle_opts=opts.LineStyleOpts(
                    color=color,
                    opacity=0.5,
                    type_="solid",
                    curve=0.2),
            )

    return c


@app.route("/")
def get_airlines_chart():
    airports_list, data = get_airports()
    c = airports_map(airports_list, data)
    c.render('airlines.html')
    return Markup(c.render_embed())


if __name__ == "__main__":
    app.run()
