from django.http import JsonResponse


from backend.models import (
    Community,
    CommunityMember,
    Post,
    PostComment,
    PostCommentLike,
)

def like_comment(request, community_id, post_id, comment_id):
    """
    Like a comment.
    :param request: session request.
    :param community_id: id of community.
    :param post_id: id of post.
    :param comment_id: id of comment.
    :return: 200 - comment liked.
             401 - permission denied.
             404 - comment not found.
             409 - conflict.
    """

    # Check if community, post and comment exists.
    try:
        community = Community.objects.get(id=community_id)
        post = Post.objects.get(id=post_id)
        comment = PostComment.objects.get(id=comment_id)
    except:
        return JsonResponse(
            "Not Found - Comment does not exist.", status=404, safe=False
        )

    user = request.user
    if CommunityMember.objects.filter(user=user, community=community).exists():
        if not PostCommentLike.objects.filter(user=user, post_comment=comment).exists():

            # Create like and add points to the comment creator.
            PostCommentLike.objects.create(user=user, post_comment=comment)
            adjust_points(
                user=user,
                points=settings.LIKE_COMMENT_PTS,
                community=community,
                post=post,
                comment=comment,
            )
            return JsonResponse("OK - Comment liked.", status=200, safe=False)

        return JsonResponse(
            "Conflict - Comment is already liked.", status=409, safe=False
        )
    return JsonResponse(
        "Unauthorized - User is not part of community.", status=401, safe=False
    )


def unlike_comment(request, community_id, post_id, comment_id):
    """
    Unlike a comment.
    :param request: session request.
    :param community_id: id of community.
    :param post_id: id of post.
    :param comment_id: id of comment.
    :return: 200 - comment liked.
             401 - permission denied.
             404 - comment not found.
    """

    # Check if community, post and comment exists.
    try:
        community = Community.objects.get(id=community_id)
        post = Post.objects.get(id=post_id)
        comment = PostComment.objects.get(id=comment_id)
    except:
        return JsonResponse(
            "Not Found - Comment does not exist.", status=404, safe=False
        )

    # Try to find like and delete it and subtract points from the post creator.
    user = request.user
    try:
        PostCommentLike.objects.get(user=user, post_comment=comment).delete()
        adjust_points(
            user=user,
            points=-settings.LIKE_COMMENT_PTS,
            community=community,
            post=post,
            comment=comment,
        )
        return JsonResponse("OK - Comment unliked.", status=200, safe=False)
    except:
        return JsonResponse(
            "Not Found - Comment does not exist.", status=404, safe=False
        )


def make_comment(request, community_id, post_id):
    """
    Add a comment.
    :param request:
    :param community_id:
    :param post_id:
    :return: 201 Created
             401 Unauthorized
             400 Bad request
             404 Not found
    """

    pass
