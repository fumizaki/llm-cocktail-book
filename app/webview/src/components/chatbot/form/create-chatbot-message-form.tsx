"use client";

import { useRouter } from "next/navigation";
import { useActionState, useEffect } from "react";
import { useToast } from "@/hooks/use-toast";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
	Select,
	SelectContent,
	SelectItem,
	SelectTrigger,
	SelectValue,
} from "@/components/ui/select";
import { createAction } from "@/server-actions/chatbot-message/create";

type Props = {
	chatbotId: string;
};

export const CreateChatbotMessageForm = ({ chatbotId }: Props) => {
	const router = useRouter();
	const { toast } = useToast();

	const [state, formAction, isPending] = useActionState(createAction, {
		inputs: {
			chatbotId: chatbotId,
			meta: {
				resource: "openai",
				mode: "discussion",
			},
			prompt: "",
		},
	});

	useEffect(() => {
		if (state.success) {
			toast({
				title: "Success",
				description: "Create Message Successfully",
			});
			router.refresh();
		} else if (state.success === false) {
			toast({
				variant: "destructive",
				title: "Error",
				description: "Error while Creating Message",
			});
		}
	}, [state]);

	return (
		<form action={formAction} className={"flex flex-col gap-3"}>
			<div className={"flex gap-1.5"}>
				<Label>
					LLM
					<Select
						key={state.inputs?.meta.resource}
						name={"inputs.meta.resource"}
						defaultValue={state.inputs?.meta.resource}
					>
						<SelectTrigger className="w-[120px]">
							<SelectValue />
						</SelectTrigger>
						<SelectContent>
							<SelectItem value="openai">OpenAI</SelectItem>
							<SelectItem value="google">Google</SelectItem>
							<SelectItem value="anthropic">Anthropic</SelectItem>
						</SelectContent>
					</Select>
				</Label>
				<Label>
					Mode
					<Select
						key={state.inputs?.meta.mode}
						name={"inputs.meta.mode"}
						defaultValue={state.inputs?.meta.mode}
					>
						<SelectTrigger className="w-[120px]">
							<SelectValue placeholder="Mode" />
						</SelectTrigger>
						<SelectContent>
							<SelectItem value="discussion">Discussion</SelectItem>
							<SelectItem value="code">Code</SelectItem>
							<SelectItem value="prompt" disabled>Prompt</SelectItem>
							<SelectItem value="summary" disabled>Summary</SelectItem>
							<SelectItem value="translation" disabled>Translation</SelectItem>
						</SelectContent>
					</Select>
				</Label>
			</div>
			<Input
				type={"hidden"}
				key={state.inputs?.chatbotId}
				name={"inputs.chatbotId"}
				defaultValue={state.inputs?.chatbotId}
			/>
			<Label>
				プロンプト
				<Input
					type={"text"}
					key={state.inputs?.prompt}
					name={"inputs.prompt"}
					defaultValue={state.inputs?.prompt}
					placeholder={"AIに相談"}
				/>
				{state.validationErrors?.title && (
					<small>{state.validationErrors?.prompt}</small>
				)}
			</Label>
			<Button type={"submit"} disabled={isPending}>
				Send Message
			</Button>
		</form>
	);
};
