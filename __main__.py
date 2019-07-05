from service.eval_service import Node, TreeParser, TreeEvaluator


if __name__ == "__main__":
    expr = '( ( 10 + 5 ) * 3 )'
    tree_parser = TreeParser(expr=expr)
    evaluator = TreeEvaluator()

    tree: Node = tree_parser.build_tree()

    s = tree.printNode('|')
    result = evaluator.resolve_tree(tree=tree)

    print(s)
    print(result)