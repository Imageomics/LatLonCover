import click
import pandas as pd
from cover.classify import add_classifications


@click.command()
@click.argument('input', type=click.Path())
@click.argument('output', type=click.Path())
@click.option('--lat-col', default="Lat", help="Latitude column name")
@click.option('--lon-col', default="Lon", help="Longitude column name")
def main(input, output, lat_col, lon_col):
    """
    Read INPUT CSV file, lookup land coverage data for a lat/lon column.
    Write OUTPUT CSV file with additional columsn for fractional land coverage data.
    """
    print(f"Reading {input}.")
    df = pd.read_csv(input)
    print("Fetching land coverage data - this may take a few minutes.")
    add_classifications(df, lat_col=lat_col, lon_col=lon_col)
    print(f"Writing {output}.")
    df.to_csv(output, index=False)
    print("Done")


if __name__ == '__main__':
    main()
