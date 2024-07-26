import glob

import pandas as pd


COLUMNS = [
    "推",
    "噓",
    "分數",
    "作者",
    "標題",
    "時間",
]

# Define functions
def get_text_file_paths() -> list[str]:
    return glob.glob(
        "/workspaces/tir102/res_gossiping/*.txt"
    )

def e_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def t_text_to_df_row_list(article_string: str) -> list[str]:
    reply_info_string = article_string.split("---split---")[1]
    return reply_info_string.split("\n")[1:-1]

def t_conbine_list_to_df(reply_info_lists: list[list]) -> pd.DataFrame:
    return pd.DataFrame(
        data=reply_info_lists,
        columns=COLUMNS,
    )

def l_df_to_csv(df: pd.DataFrame) -> None:
    df.to_csv("ptt_2.csv", index=0)


if __name__ == "__main__":
    # Get paths of all text files
    path_list = get_text_file_paths()

    # Loop for file paths
    data = []
    for path in path_list:
        # Extract text file
        article_string = e_text_file(path)

        # Text to list-element in DataFrame
        reply_info_list = t_text_to_df_row_list(article_string)
        data.append(reply_info_list)

    # Concat lists to DataFrame
    df = t_conbine_list_to_df(data)

    # Load DataFrame to CSV
    l_df_to_csv(df)
