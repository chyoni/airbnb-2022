from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from conversations import forms
from users import models as user_models
from . import models


def go_conversations(request, u1_pk, u2_pk):

    try:
        u1 = user_models.User.objects.get(pk=u1_pk)
        u2 = user_models.User.objects.get(pk=u2_pk)

        try:
            chat_room = (
                models.Conversation.objects.filter(participants=u1)
                .filter(participants=u2)
                .get()
            )
            return redirect(
                reverse(
                    "conversations:detail", kwargs={"conversation_pk": chat_room.pk}
                )
            )
        except models.Conversation.DoesNotExist:
            chat_room = models.Conversation.objects.create()
            chat_room.add(u1, u2)
            chat_room.save()
            return redirect(
                reverse(
                    "conversations:detail", kwargs={"conversation_pk": chat_room.pk}
                )
            )
    except user_models.User.DoesNotExist:
        return render(request, "404.html")


def conversation_detail(request, conversation_pk):

    try:
        conversation = models.Conversation.objects.get(pk=conversation_pk)

        return render(
            request, "conversations/detail.html", {"conversation": conversation}
        )
    except models.Conversation.DoesNotExist:
        return render(request, "404.html")


def send(request, conversation_pk):

    try:
        conversation = models.Conversation.objects.get(pk=conversation_pk)

        if request.method == "POST":

            form = forms.SendForm(request.POST)

            if form.is_valid():
                print("????")
                form.save(user=request.user, conversation=conversation)
                return redirect(
                    reverse(
                        "conversations:detail",
                        kwargs={"conversation_pk": conversation_pk},
                    )
                )

            messages.error(
                request, "Message sending error. Please check the form is valid"
            )
            return redirect(
                reverse(
                    "conversations:detail", kwargs={"conversation_pk": conversation_pk}
                )
            )

    except models.Conversation.DoesNotExist:
        return render(request, "404.html")
