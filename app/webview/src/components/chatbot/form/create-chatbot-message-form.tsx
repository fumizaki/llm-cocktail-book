"use client";

import { cn } from "@/lib/style";
import { useRouter } from "next/navigation";
import { useActionState, useEffect } from "react";
import { useToast } from "@/hooks/use-toast";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import {
	Select,
	SelectContent,
	SelectItem,
	SelectTrigger,
	SelectValue,
} from "@/components/ui/select";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { createAction } from "@/server-actions/chatbot-message/create";

type Props = {
	chatbotId: string;
	className?: string;
};

export const CreateChatbotMessageForm = ({ chatbotId, className }: Props) => {
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
		<form
			action={formAction}
			className={cn(
				`w-full flex flex-col justify-center items-center`,
				className,
			)}
		>
			<Card className={`w-full`}>
				<CardHeader>
					<CardTitle>Chat</CardTitle>
				</CardHeader>
				<CardContent className="flex flex-col gap-3">
					<div className={"flex gap-1.5"}>
						<Label className={'flex flex-col gap-1.5'}>
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
						<Label className={'flex flex-col gap-1.5'}>
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
									<SelectItem value="prompt" disabled>
										Prompt
									</SelectItem>
									<SelectItem value="summary" disabled>
										Summary
									</SelectItem>
									<SelectItem value="translation" disabled>
										Translation
									</SelectItem>
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
					<Label className={'flex flex-col gap-1.5'}>
						プロンプト
						<Textarea
							className={"resize-none h-full"}
							key={state.inputs?.prompt}
							name={"inputs.prompt"}
							defaultValue={state.inputs?.prompt}
							placeholder={"AIに相談"}
						/>
						{state.validationErrors?.prompt && (
							<small>{state.validationErrors?.prompt}</small>
						)}
					</Label>
					<Button type={"submit"} disabled={isPending}>
						Send Message
					</Button>
				</CardContent>
			</Card>
		</form>
	);
};
