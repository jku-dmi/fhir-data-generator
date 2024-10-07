import time
from factory.fhir_data_factory import generate_data_random_references_to_server
from util.abfragen import abfrage1, abfrage2, abfrage3, abfrage4


def main():
    # start_time = time.time()
    # print(abfrage10())
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print(f"elapsed_time: {elapsed_time}")
    generate_data_random_references_to_server(10, 10, 10, 10,
                                              10, 10,
                                              10,
                                              100,
                                              10,
                                              1000)


if __name__ == "__main__":
    main()
