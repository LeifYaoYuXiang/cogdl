from cogdl import experiment
from cogdl.utils import build_args_from_dict, print_result, set_random_seed, get_extra_args

DATASET_REGISTRY = {}


def default_parameter():
    args = {
        "hidden_size": 128,
        "cpu": True,
        "seed": [0, 1, 2],
        "walk_length": 80,
        "walk_num": 40,
        "negative": 5,
        "batch_size": 1000,
        "alpha": 0.025,
    }
    return build_args_from_dict(args)


def register_func(name):
    def register_func_name(func):
        DATASET_REGISTRY[name] = func
        return func

    return register_func_name


@register_func("gtn-dblp")
def dblp_config(args):
    return args


@register_func("gtn-acm")
def acm_config(args):
    return args


@register_func("gtn-imdb")
def imdb_config(args):
    return args


def run(dataset_name):
    args = default_parameter()
    args = DATASET_REGISTRY[dataset_name](args).__dict__
    results = experiment(task="multiplex_node_classification", dataset=dataset_name, model="pte", **args)
    return results


if __name__ == "__main__":
    datasets = ["gtn-dblp", "gtn-acm", "gtn-imdb"]
    for x in datasets:
        run(x)
