import pandas as pd


def rename_columns(input_file, output_file='final_clean_data.csv'):
    """
    重命名列：new_movie_id -> movie_id, new_user_id -> user_id
    """

    # 读取数据
    df = pd.read_csv(input_file)

    print(f"读取文件: {input_file}")
    print(f"原始列名: {list(df.columns)}")

    # 重命名映射
    rename_dict = {
        'new_movie_id': 'movie_id',
        'new_user_id': 'user_id'
    }

    # 只重命名实际存在的列
    existing_rename = {old: new for old, new in rename_dict.items() if old in df.columns}

    if existing_rename:
        df = df.rename(columns=existing_rename)
        print(f"重命名的列: {existing_rename}")
    else:
        print("未找到需要重命名的列")

    # 保存结果
    df.to_csv(output_file, index=False)

    print(f"\n重命名后的列名: {list(df.columns)}")
    print(f"结果已保存到: {output_file}")

    # 显示前几条记录
    print(f"\n数据示例 (前3条):")
    print(df.head(3).to_string(index=False))

    return df


# 使用
if __name__ == "__main__":
    rename_columns('clean_final_data.csv', 'smalldata.csv')