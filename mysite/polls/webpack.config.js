const path = require("path");
const webpack = require("webpack");
// ここでdotenvを使いたい場合は右を参照: https://blog.ojisan.io/webpack-env-var/

module.exports = (env, argv) => {
    // `mode` is `'XX'` if you ran webpack like so: `webpack watch --mode XX` (v5 syntax)
    const mode = argv.mode || 'development'

    return {
        entry: "./src/index.js",
        output: {
            path: path.resolve(__dirname, "./static/frontend"),
            filename: "[name].js",
        },
        module: {
            rules: [
                {
                    test: /\.js$/,
                    exclude: /node_modules/,
                    use: {
                        loader: "babel-loader",
                    },
                },
            ],
        },
        optimization: {
            minimize: true,
        },
        // グローバル環境変数が定義できる
        plugins: [
            new webpack.DefinePlugin({
                'process.env.NODE_ENV' : JSON.stringify(mode)
            })
        ]
    }
}
