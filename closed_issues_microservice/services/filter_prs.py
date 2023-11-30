#Filter-out PR's
def filter_out_prs(all_issues):
    filtered_issues = []
    for issue in all_issues:
        if "pull_request" not in issue:
            filtered_issues.append(issue)
    return filtered_issues